from django.shortcuts import render

from Petstagram_project.photos.models import PhotoPet


def home_page(request):
    context = {
        "photos_of_pet": PhotoPet.objects.all(),
    }

    return render(request, "common/home-page.html", context)
