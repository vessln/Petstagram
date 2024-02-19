from django.shortcuts import render
from django.urls import reverse

from django.views import generic as views

from Petstagram_project.photos.forms import CreatePhotoForm, UpdatePhotoForm
from Petstagram_project.photos.models import PhotoPet


class CreatePhotoView(views.CreateView):
    queryset = PhotoPet.objects.all().prefetch_related("pets")

    form_class = CreatePhotoForm

    template_name = "photos/create-photo-page.html"

    def get_success_url(self):
        return reverse("details photo",
                       kwargs={"pk": self.object.pk})


class DetailsPhotoView(views.DetailView):
    # model = PhotoPet
    queryset = PhotoPet.objects.all().prefetch_related("pets"
                ).prefetch_related("photolike_set"
                ).prefetch_related("photocomment_set")

    template_name = "photos/details-photo-page.html"

    # "photo_pet": PhotoPet.objects.get(pk=pk)


class EditPhotoView(views.UpdateView):
    queryset = PhotoPet.objects.all().prefetch_related("pets")

    form_class = UpdatePhotoForm

    template_name = "photos/edit-photo-page.html"


