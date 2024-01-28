from django.shortcuts import render


def create_photo(request):
    context = {}

    return render(request, "photos/create-photo-page.html")


def details_photo(request, pk):
    contex = {}

    return render(request, "photos/details-photo-page.html")


def edit_photo(request, pk):
    context = {}

    return render(request, "photos/edit-photo-page.html")
