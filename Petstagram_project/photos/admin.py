from django.contrib import admin

from Petstagram_project.photos.models import PhotoPet


@admin.register(PhotoPet)
class PhotoPetAdmin(admin.ModelAdmin):
    pass
