from django.urls import path, include

from Petstagram_project.accounts.views import signup_user, signin_user, signout_user, show_details_profile, \
    edit_profile, delete_profile

urlpatterns = (
    path("signup/", signup_user, name="signup"),
    path("signin/", signin_user, name="signin"),
    path("signout/", signout_user, name="signout"),
    path("profile/<int:pk>/",
         include([
             path("", show_details_profile, name="details profile"),
             path("edit/", edit_profile, name="edit profile"),
             path("delete/", delete_profile, name="delete profile"),
                ]),
         ),

)
