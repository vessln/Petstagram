from django.urls import path

from Petstagram_project.common.views import home_page, like_pet_photo

urlpatterns = (
    path("", home_page, name="home page"),
    path("like_pet_photo/<int:pk>/", like_pet_photo, name="like pet photo")

)