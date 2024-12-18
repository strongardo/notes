from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def reg(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('notes')

    form = UserRegistrationForm()
    return render(request, 'reg.html', context={'form': form})
