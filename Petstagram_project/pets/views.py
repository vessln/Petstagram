from django.shortcuts import render


def create_pet(request):
    context = {}

    return render(request, "pets/create-pet-page.html")


def details_pet(request, username, pet_slug):
    context = {}

    return render(request, "pets/details-pet-page.html")


def edit_pet(request, username, pet_slug):
    context = {}

    return render(request, "pets/edit-pet-page.html")


def delete_pet(request, username, pet_slug):
    context = {}

    return render(request, "pets/delete-pet-page.html")

