from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram_project.pets.models import Pet


class PhotoPet(models.Model):
    MAX_LENGTH_DESCR = 300
    MIN_LENGTH_DESCR = 10
    MAX_LENGTH_LOCATION = 30

    photo = models.ImageField(
        upload_to="photos_pet/",
        null=False,
        blank=False,
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

    modified_at = models.DateTimeField(auto_now=True)   # every time when model is modified