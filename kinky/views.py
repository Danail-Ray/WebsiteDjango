from django.shortcuts import render, redirect
from django.views import View

from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect


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


class Profile(View):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404("User does not exist")

        return render(request, self.template_name, {'user': user})


def all_users(request):
    users = User.objects.all()
    return render(request, 'allUsers.html', {'users': users})


def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    request.user.profile.following.add(user_to_follow)
    return redirect('profile_detail', user_id=user_id)

