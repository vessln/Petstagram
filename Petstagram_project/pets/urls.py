from django.urls import path, include

from Petstagram_project.pets.views import CreatePetView, DetailsPetView, EditPetView, DeletePetView

urlpatterns = (
    path("create/", CreatePetView.as_view(), name="create pet"),
    path("<str:username>/pet/<slug:pet_slug>/",
         include([
             path("", DetailsPetView.as_view(), name="details pet"),
             path("edit/", EditPetView.as_view(), name="edit pet"),
             path("delete/", DeletePetView.as_view(), name="delete pet"),
        ]),
    ),

)