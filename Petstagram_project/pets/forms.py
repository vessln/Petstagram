from django import forms
from django.core.exceptions import ValidationError

from Petstagram_project.core.forms_mixins import ReadonlyFormFieldsMixin
from Petstagram_project.pets.models import Pet


class BasePetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ("name", "birth_date", "pet_photo",)

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Pet name"}),
            "birth_date": forms.DateInput(attrs={"type": "date"}),
            "pet_photo": forms.TextInput(attrs={"placeholder": "Link to image"}),
        }

        labels = {
            "name": "Pet name",
            "birth_date": "Date of birth",
        }


class CreatePetForm(BasePetForm):
    pass


class EditPetForm(ReadonlyFormFieldsMixin, BasePetForm):
    readonly_fields = ("birth_date", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._make_fields_readonly()

    def clean_birth_date(self):
        # birth_date = self.cleaned_data["birth_date"]
        # if birth_date != self.instance.birth_date:
        #     raise ValidationError("Date of birth cannot be changed!")

        return self.instance.birth_date


class DeletePetForm(ReadonlyFormFieldsMixin, BasePetForm):
    readonly_fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._make_fields_readonly()

    def save(self, commit=True):
        if commit:
            # self.instance.likes.delete()
            # self.instance.comments.delete()
            self.instance.delete()

        return self.instance


