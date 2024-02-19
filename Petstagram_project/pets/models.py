from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    MAX_LENGTH_NAME = 30
    MAX_LENGTH_PHOTO_URL = 600

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
    )

    pet_photo = models.URLField(
        null=True,
        blank=True,
        max_length=MAX_LENGTH_PHOTO_URL,
    )

    birth_date = models.DateField()

    slug = models.SlugField(  # for SEO
        unique=True,
        null=False,   # cannot be null in DB
        blank=True,   # user can submit without fill in this field in form
        editable=False,  # only in the app - user cannot see this field (not in DB)
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # to generate pk

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.pk}")  # generate valid slug
        super().save(*args, **kwargs)  # save generated slug with name and pk

    def __str__(self):
        return self.name






