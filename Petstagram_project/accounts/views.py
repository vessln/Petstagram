from django.shortcuts import render, redirect


def signup_user(request):
    context = {}

    return render(request, "accounts/signup_user_page.html", context)


def signin_user(request):
    context = {}

    return render(request, "accounts/signin_user_page.html", context)


def signout_user(request):

    return redirect("home page")


def show_details_profile(request, pk):
    context = {}

    return render(request, "accounts/show_details_profile_page.html", context)


def edit_profile(request, pk):
    context = {}

    return render(request, "accounts/edit_profile_page.html", context)


def delete_profile(request, pk):
    context = {}

    return render(request, "accounts/delete_profile_page.html", context)

