from django import forms

from Petstagram_project.core.mixins import ReadonlyFormFieldsMixin
from Petstagram_project.photos.models import PhotoPet


class BasePhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoPet
        fields = ("photo", "description", "location", "pets",)


class CreatePhotoForm(BasePhotoForm):
    pass


class UpdatePhotoForm(ReadonlyFormFieldsMixin, BasePhotoForm):
    readonly_fields = ("photo", "pets")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._make_fields_readonly()
        self.fields["pets"].required = False




