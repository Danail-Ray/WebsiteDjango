from django.contrib import messages
from django.views import View
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, JsonResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
import os
from .models import UserProfile, Follow
from .models import ImagesFromUser


def login_view(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Check if a user with the provided username or email already exists
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                # Handle the case when the user already exists
                return render(request, 'login.html',
                              {'form': form, 'error_message': 'Username or email already exists.'})

            # Save the user to the database
            user = form.save()

            # create folder for image upload
            folder_path = os.path.join(settings.MEDIA_ROOT, str(user), 'images')
            if not os.path.exists(folder_path):
                # If not, create the folder
                os.makedirs(folder_path)
                print(f"Folder '{folder_path}' created successfully.")
            else:
                print(f"Folder '{folder_path}' already exists.")

            # Log the user in
            login(request, user)
            return redirect('landing')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


@login_required(login_url='login')  # Redirect to signup page if not authenticated
def landing(request):
    return render(request, 'landing.html')


def response_error_handler(request, exception=None):
    return HttpResponse("Error handler content", status=403)


def permission_denied_view(request):
    raise PermissionDenied


class UserProfileView(View):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        user = get_object_or_404(User, username=username)

        images_folder_path = os.path.join(settings.MEDIA_ROOT, str(user), 'images')
        image_files = [f for f in os.listdir(images_folder_path) if os.path.isfile(os.path.join(images_folder_path, f))]
        full_paths = [os.path.join(images_folder_path, f).replace("\\", "/") for f in image_files]
        images_from_user = ImagesFromUser.objects.filter(user=user)

        following = Follow.objects.filter(follower=request.user, following=user)
        is_following = following.exists()

        return render(request, self.template_name, {'viewed_user': user,
                                                    'image_files': image_files, 'full_paths': full_paths,
                                                    'images_from_user': images_from_user, 'is_following': is_following})


def all_users(request):
    users = User.objects.all()
    return render(request, 'allUsers.html', {'users': users})


def update_bio_view(request):
    try:
        if request.method == 'POST':
            user = request.user
            text_value = request.POST.get('bioValue')
            user.user.bio = text_value
            user.user.save()
            # Add any additional context data you need for the 'profile.html' template
            context = {
                'user': request.user,
                # Add other context data as needed
            }
            return render(request, 'profile.html', context)
    except Exception as e:
        # Handle exceptions if needed
        print(f"An error occurred: {e}")
        return redirect('landing')  # Provide a default URL in case of an error


def upload_photo(request, username):
    try:
        if request.method == 'POST':
            image = request.FILES.get('imageContainer')  # Use request.FILES for file uploads
            user = request.user
            image.name = str(user) + '.jpg'

            images_user = ImagesFromUser(user=request.user, image=image)
            images_user.save()

            user.user.image_counter += 1
            user.user.save()

            messages.success(request, 'Photo uploaded successfully!')
            return redirect('profile', username=request.user.username)
    except Exception as e:
        # Handle exceptions if needed
        print(f"An error occurred: {e}")
        return redirect('landing')  # Provide a default URL in case of an error


def get_data(request):
    data = UserProfile.objects.values()
    return JsonResponse(list(data), safe=False)


def follow_user(request, username):
    try:
        if request.method == 'POST':
            user = request.user
            user_profile = get_object_or_404(User, username=username)
            following = Follow.objects.filter(follower=user, following=user_profile)
            print(following)

            if not following.exists():
                follow = Follow(follower=user, following=user_profile)
                user.user.following_count += 1
                user_profile.user.followers_count += 1
                follow.save()
            else:
                following.delete()
                user.user.following_count -= 1
                user_profile.user.followers_count -= 1

            user.user.save()
            user_profile.user.save()
            messages.success(request, 'Photo uploaded successfully!')
            return redirect('profile', username=username)
    except Exception as e:
        # Handle exceptions if needed
        print(f"An error occurred: {e}")
        return redirect('landing')  # Provide a default URL in case of an error


def upload_profile(request):
    try:
        if request.method == 'POST':
            image = request.FILES.get('profile_image')  # Use request.FILES for file uploads
            print(image)
            user = request.user
            user.user.profile_image.delete()
            user.user.profile_image = image
            user.user.save()
            messages.success(request, 'Photo uploaded successfully!')
            return redirect('profile', username=request.user.username)
    except Exception as e:
        # Handle exceptions if needed
        print(f"An error occurred: {e}")
        return redirect('landing')  # Provide a default URL in case of an error


@login_required
def delete_photo(request, photo_id, username):
    user = request.user
    image = ImagesFromUser.objects.get(id=photo_id)
    image.delete()
    user.user.image_counter -= 1
    user.user.save()
    print("-------------------")
    print(image.image.name)

    try:
        os.remove(os.path.join(settings.MEDIA_ROOT, image.image.name))
    except FileNotFoundError:
        pass  # Image file doesn't exist locally, no need to delete

    return redirect('profile', username=username)


@login_required
def feed(request):
    user = request.user
    all_images = ImagesFromUser.objects.all()
    first = all_images.first()
    id = first.id
    print(id)
    return render(request, 'feed.html', {'user': user, 'all_images': all_images})
