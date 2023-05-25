from django.shortcuts import render
from .data_source import find_user


def user_details(request):
    user = None
    if request.method == "POST":
        name = request.POST.get("name")
        user = find_user(name)
    return render(request, "users.html", {"user": user})
