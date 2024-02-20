from django.urls import path, include

from Petstagram_project.photos.views import CreatePhotoView, DetailsPhotoView, EditPhotoView

urlpatterns = (
    path("create/", CreatePhotoView.as_view(), name="create photo"),
    path("<int:pk>/",
         include([
             path("", DetailsPhotoView.as_view(), name="details photo"),
             path("edit/", EditPhotoView.as_view(), name="edit photo"),
                ]),
        ),

)

