from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram_project.pets.models import Pet
from Petstagram_project.photos.validators import MaxSizeImageValidator

UserModel = get_user_model()


class PhotoPet(models.Model):
    MAX_LENGTH_DESCR = 300
    MIN_LENGTH_DESCR = 10
    MAX_LENGTH_LOCATION = 30
    MAX_SIZE_3_MB = 3 * 1024 * 2024

    photo = models.ImageField(
        upload_to="photos_pet/",
        null=False,
        blank=False,
        validators=[MaxSizeImageValidator(limit_value=MAX_SIZE_3_MB),],
    )

    description = models.CharField(
        max_length=MAX_LENGTH_DESCR,  # executed at the DB level (final check, after server validations)
        validators=[MinLengthValidator(MIN_LENGTH_DESCR),],  # executed at the server level
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LENGTH_LOCATION,
        null=True,
        blank=True,
    )

    pets = models.ManyToManyField(Pet,)

    created_at = models.DateTimeField(auto_now_add=True,)  # when the model is created

    modified_at = models.DateTimeField(auto_now=True,)  # every time when model is modified

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return f"{', '.join(f'{pet.name} - {self.description}' for pet in self.pets.all())}"
