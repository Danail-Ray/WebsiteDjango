from django.views import View
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import UserProfile


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
        return render(request, self.template_name, {'viewed_user': user})

def all_users(request):
    users = User.objects.all()
    return render(request, 'allUsers.html', {'users': users})


def user_profile_view(request, username):
    viewed_user = get_object_or_404(User, username=username)
    user_profile = UserProfileView.objects.get(user=viewed_user)
    return render(request, 'profile.html', {'viewed_user': viewed_user, 'user_profile': user_profile})


def update_bio_view(request):
    try:
        if request.method == 'POST':
            user = request.user
            text_value = request.POST.get('bioValue')
            user.user.bio = text_value
            user.user.save()

        # Redirect to the user's profile view after updating bio
        return redirect('user_profile', username=user.username)
    except Exception as e:
        # Handle exceptions if needed
        print(f"An error occurred: {e}")
        return redirect('landing')  # Provide a default URL in case of an error


def upload_photo(request):
    try:
        if request.method == 'POST':
            user = request.user
            image = request.FILES.get('image')
            user.user.image = image
            user.user.save()

        # Redirect to the user's profile view after uploading photo
        return redirect('user_profile', username=user.username)
    except Exception as e:
        # Handle exceptions if needed
        print(f"An error occurred: {e}")
        return redirect('landing')  # Provide a default URL in case of an error
    
    
def show_images(request):
    profiles = UserProfile.objects.all()    
    return render(request, 'profile.html', {'user_profiles': profiles})
    