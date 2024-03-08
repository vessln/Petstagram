from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from Petstagram_project.accounts.forms import PetstagramUserCreationForm, ProfileUpdateForm
from Petstagram_project.accounts.models import Profile


class SignInUserView(auth_views.LoginView):
    template_name = "accounts/signin_user_page.html"
    redirect_authenticated_user = True  # the logged-in user cannot access login page


class SignUpUserView(views.CreateView):
    form_class = PetstagramUserCreationForm
    template_name = "accounts/signup_user_page.html"
    success_url = reverse_lazy("home page")

    def form_valid(self, form):
        # form_valid method will call save method
        result = super().form_valid(form)
        login(self.request, form.instance)

        return result


def signout_user(request):
    logout(request)

    return redirect("home page")


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects.prefetch_related("user").all()
    template_name = "accounts/show_details_profile_page.html"


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    form_class = ProfileUpdateForm
    template_name = "accounts/edit_profile_page.html"

    def get_success_url(self):
        return reverse("details profile",
                       kwargs={"pk": self.object.pk})

    # def get_form(self, form_class=None):   # if I don't make ModelForm:
    #     form = super().get_form(form_class=form_class)
    #
    #     form.fields["date_of_birth"].widget.attrs["type"] = "date"
    #
    #     return form


class ProfileDeleteView(views.UpdateView):
    queryset = Profile.objects.all()

    template_name = "accounts/delete_profile_page.html"

