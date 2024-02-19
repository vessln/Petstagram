from django.urls import path

from Petstagram_project.common.views import HomePageView, like_pet_photo

urlpatterns = (
    path("", HomePageView.as_view(), name="home page"),
    path("like_pet_photo/<int:pk>/", like_pet_photo, name="like pet photo"),

)