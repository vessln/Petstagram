from django.shortcuts import redirect

from django.urls import reverse, reverse_lazy
from django.views import generic as views

from Petstagram_project.common.models import PhotoLike
from Petstagram_project.photos.models import PhotoPet


class HomePageView(views.ListView):
    # model = PhotoPet
    queryset = PhotoPet.objects.all(
                ).prefetch_related("pets"
                ).prefetch_related("photolike_set")

    template_name = "common/home-page.html"

    paginate_by = 1

    # def get_queryset(self):
        # queryset = super().get_queryset()
        # pet_name_pattern = self.request.GET.get("pet_name_pattern", None)
        # if pet_name_pattern:
        #     queryset = PhotoPet.objects.filter(pets__name__icontains=pet_name_pattern)
        # return queryset

        # if I have a lot of things to filter:

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["pet_name_pattern"] = self.request.GET.get("pet_name_pattern", None) or ""

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_pet_name(queryset)

        return queryset

    def filter_pet_name(self, queryset):
        pet_name_pattern = self.request.GET.get("pet_name_pattern", None)
        filter_query = {}

        if pet_name_pattern:
            filter_query["pets__name__icontains"] = pet_name_pattern

        return queryset.filter(**filter_query)



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




