from django.contrib import admin
from django.urls import path, include


urlpatterns = (
    path("admin/", admin.site.urls),
    path("", include("Petstagram_project.common.urls")),
    path("accounts/", include("Petstagram_project.accounts.urls")),
    path("pets/", include("Petstagram_project.pets.urls")),
    path("photos/", include("Petstagram_project.photos.urls")),

)
