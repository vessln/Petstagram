from django import forms

from Petstagram_project.photos.models import PhotoPet


class BasePhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoPet
        fields = ("photo", "description", "location", "pets",)


class CreatePhotoForm(BasePhotoForm):
    pass


class UpdatePhotoForm(BasePhotoForm):
    pass