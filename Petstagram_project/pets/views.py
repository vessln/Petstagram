from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from Petstagram_project.pets.forms import CreatePetForm, EditPetForm, DeletePetForm
from Petstagram_project.pets.models import Pet


class CreatePetView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = CreatePetForm
    template_name = "pets/create-pet-page.html"

    def get_success_url(self):
        return reverse("details pet",
                       kwargs={"username": "vesi",
                               "pet_slug": self.object.slug})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.instance.user = self.request.user

        return form

    # or:
    # def form_valid(self, form):
    #     pet = form.save(commit=False)
    #     pet.user = self.request.user
    #     return super().form_valid(form)


class DetailsPetView(auth_mixins.LoginRequiredMixin, views.DetailView):
    # model = Pet
    queryset = Pet.objects.all(
                ).prefetch_related("photopet_set"
                ).prefetch_related("photopet_set__photolike_set"
                ).prefetch_related("photopet_set__pets")

    template_name = "pets/details-pet-page.html"
    slug_url_kwarg = "pet_slug"  # parameter's name in URLs.py
    # slug_field = "..."  field's name in Model


class EditPetView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Pet  # or queryset = Pet.objects.all()
    form_class = EditPetForm
    template_name = "pets/edit-pet-page.html"
    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["username"] = "Vesi"

        return context

    def get_success_url(self):
        return reverse("details pet",
                       kwargs={"username": self.request.GET.get("username"),  # or self.kwargs["username"]
                               "pet_slug": self.object.slug})  # or self.kwargs["pet_slug"]


class DeletePetView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Pet
    form_class = DeletePetForm

    template_name = "pets/delete-pet-page.html"

    slug_url_kwarg = "pet_slug"

    success_url = reverse_lazy("home page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["username"] = "Vesi"

        form = self.form_class(instance=self.object)
        context["form"] = form

        return context

    # get_context_data()  OR  extra_context + get_form_kwargs():

    # extra_context = {"username": "Vesi",}

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["instance"] = self.object
    #     return kwargs


