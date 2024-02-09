from django.shortcuts import render, redirect

from Petstagram_project.pets.forms import CreatePetForm, EditPetForm, DeletePetForm
from Petstagram_project.pets.models import Pet


def create_pet(request):
    pet_form = CreatePetForm(request.POST or None)

    if request.method == "POST":
        if pet_form.is_valid():
            created_pet = pet_form.save()

            return redirect("details pet", username="vesi", pet_slug=created_pet.slug)

    context = {
        "pet_form": pet_form,
    }

    return render(request, "pets/create-pet-page.html", context)


def details_pet(request, username, pet_slug):
    context = {
        "pet": Pet.objects.get(slug=pet_slug)
    }

    return render(request, "pets/details-pet-page.html", context)


def edit_pet(request, username, pet_slug):
    current_pet = Pet.objects.filter(slug=pet_slug).get()

    pet_form = EditPetForm(request.POST or None, instance=current_pet)

    if request.method == "POST":
        if pet_form.is_valid():
            pet_form.save()

            return redirect("details pet", username=username, pet_slug=pet_slug)

    context = {
        "pet_form": pet_form,
        "username": username,
        "pet": current_pet,
    }

    return render(request, "pets/edit-pet-page.html", context)


def delete_pet(request, username, pet_slug):
    current_pet = Pet.objects.filter(slug=pet_slug).get()

    pet_form = DeletePetForm(request.POST or None, instance=current_pet)

    if request.method == "POST":
        pet_form.save()
        return redirect("home page")

    context = {
        "pet_form": pet_form,
        "username": username,
        "pet": current_pet,
    }

    return render(request, "pets/delete-pet-page.html", context)

