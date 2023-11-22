from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # home sozun programin esas oknosuna url yaz
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
