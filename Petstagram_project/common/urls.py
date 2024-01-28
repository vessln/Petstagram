from django.urls import path

from Petstagram_project.common.views import home_page

urlpatterns = (
    path("", home_page, name="home page"),

)