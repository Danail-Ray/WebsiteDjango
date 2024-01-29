from django import forms
from django.contrib.auth import get_user_model
from .models import UserProfile


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        User = get_user_model()
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['name']
        )
        user.set_password(self.cleaned_data['password'])
        user.save()

        # Create UserProfile and associate it with the user
        UserProfile.objects.create(
            user=user,
        )

        return user

