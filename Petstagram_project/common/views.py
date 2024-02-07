from django.shortcuts import render, redirect

from Petstagram_project.common.models import PhotoLike
from Petstagram_project.photos.models import PhotoPet


def home_page(request):
    context = {
        "photos_of_pet": PhotoPet.objects.all(),
    }

    return render(request, "common/home-page.html", context)


def like_pet_photo(request, pk):

    # photo_pet = PhotoPet.objects.get(pk=pk, user=request.user)
    # photo_pet = PhotoPet.objects.get(pk=pk)
    # pet_photo_like =PhotoLike.objects.filter(pk=pk).first()
    pet_photo_like = PhotoLike.objects.filter(photo_pet_id=pk).first()

    if pet_photo_like:
        pet_photo_like.delete()  # logic for dislike
    else:
        PhotoLike.objects.create(photo_pet_id=pk)  # logic for like

    return redirect(request.META.get("HTTP_REFERER"))




