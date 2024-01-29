from django.contrib import admin

from Petstagram_project.photos.models import PhotoPet


@admin.register(PhotoPet)
class PhotoPetAdmin(admin.ModelAdmin):
    list_display = ("pk", "names_of_tagged_pets", "short_description", "date_created")

    def names_of_tagged_pets(self, obj):
        return ', '.join(p.name for p in obj.pets.all())

    def short_description(self, obj):
        return obj.description[:10]

    def date_created(self, obj):
        return obj.created_at.strftime('%A %d.%m.%Y')