from django.urls import path, include

from Petstagram_project.photos.views import CreatePhotoView, DetailsPhotoView, edit_photo

urlpatterns = (
    path("create/", CreatePhotoView.as_view(), name="create photo"),
    path("<int:pk>/",
         include([
             path("", DetailsPhotoView.as_view(), name="details photo"),
             path("edit/", edit_photo, name="edit photo"),
            ]),
        ),

)