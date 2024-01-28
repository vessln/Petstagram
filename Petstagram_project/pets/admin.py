from django.contrib import admin

from Petstagram_project.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("slug", "name", "birth_date")
