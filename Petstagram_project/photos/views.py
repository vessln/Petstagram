from django.shortcuts import render

from Petstagram_project.photos.models import PhotoPet


def create_photo(request):
    context = {}

    return render(request, "photos/create-photo-page.html", context)


def details_photo(request, pk):
    context = {
        "photo_pet": PhotoPet.objects.get(pk=pk),
    }

    return render(request, "photos/details-photo-page.html", context)


def edit_photo(request, pk):
    context = {}

    return render(request, "photos/edit-photo-page.html", context)
