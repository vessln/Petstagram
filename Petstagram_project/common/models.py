from django.db import models

from Petstagram_project.photos.models import PhotoPet


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
        on_delete=models.DO_NOTHING,
    )


class PhotoLike(models.Model):

    photo_pet = models.ForeignKey(
        PhotoPet,
        on_delete=models.DO_NOTHING,
    )

