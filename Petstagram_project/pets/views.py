from django.shortcuts import render

from Petstagram_project.pets.models import Pet


def create_pet(request):
    context = {}

    return render(request, "pets/create-pet-page.html", context)


def details_pet(request, username, pet_slug):
    context = {
        "pet": Pet.objects.get(slug=pet_slug)
    }

    return render(request, "pets/details-pet-page.html", context)


def edit_pet(request, username, pet_slug):
    context = {}

    return render(request, "pets/edit-pet-page.html", context)


def delete_pet(request, username, pet_slug):
    context = {}

    return render(request, "pets/delete-pet-page.html", context)

