from django.contrib.auth import get_user_model
from django.db import models

from Petstagram_project.photos.models import PhotoPet

UserModel = get_user_model()


class PhotoComment(models.Model):
    MAX_LENGTH_TEXT = 300

    text = models.CharField(
        max_length=MAX_LENGTH_TEXT,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )

    photo_pet = models.ForeignKey(
        PhotoPet,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class PhotoLike(models.Model):

    photo_pet = models.ForeignKey(
        PhotoPet,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

