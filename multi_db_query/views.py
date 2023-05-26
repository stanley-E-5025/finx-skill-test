from django.shortcuts import render
from .data_source import find_user
from .forms import SearchForm


def user_details(request):
    user = None
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            user = find_user(name)

        return render(request, "users.html", {"form": form, "user": user})

    if request.method == "GET":
        form = SearchForm()
        return render(request, "users.html", {"form": form, "user": user})
