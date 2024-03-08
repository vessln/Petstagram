from django.urls import path, include

from Petstagram_project.accounts.views import SignUpUserView, SignInUserView, signout_user, \
    ProfileUpdateView, ProfileDeleteView, ProfileDetailsView

urlpatterns = (
    path("signup/", SignUpUserView.as_view(), name="signup"),
    path("signin/", SignInUserView.as_view(), name="signin"),
    path("signout/", signout_user, name="signout"),
    path("profile/<int:pk>/",
         include([
             path("", ProfileDetailsView.as_view(), name="details profile"),
             path("edit/", ProfileUpdateView.as_view(), name="edit profile"),
             path("delete/", ProfileDeleteView.as_view(), name="delete profile"),
                ]),
         ),

)
