from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from Petstagram_project.accounts.models import Profile

UserModel = get_user_model()


class PetstagramUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ("email", )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "date_of_birth", "profile_picture",)

        labels = {
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "date_of_birth": "Date of birth:",
            "profile_picture": "Profile picture:",
        }

        widgets = {
            "date_of_birth": forms.DateInput(attrs={
                "placeholder": "year-month-day"
            }),
        }