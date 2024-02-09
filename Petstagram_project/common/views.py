from django.shortcuts import render, redirect

from Petstagram_project.common.models import PhotoLike
from Petstagram_project.photos.models import PhotoPet


def home_page(request):
    pet_name_pattern = request.GET.get("pet_name_pattern", None)
    pet_photos = PhotoPet.objects.all()

    if pet_name_pattern:
        pet_photos = PhotoPet.objects.filter(pets__name__icontains=pet_name_pattern)

    context = {
        "photos_of_pets": pet_photos,
        "pet_name_pattern": pet_name_pattern,
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

    return redirect(request.META.get("HTTP_REFERER") + f"#photo-{pk}")




