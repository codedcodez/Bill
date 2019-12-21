from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserForm


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.save()

            messages.success(request, "You have registered succcessfully!")

            return redirect("login")

    else:
        user_form = UserForm()

    context = {
        'user_form': user_form,
    }

    return render(request, 'user_accounts/signup.html', context)
