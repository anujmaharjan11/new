from django.shortcuts import render, redirect
from .forms import UserRegister
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'student/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account is created - {username}')
            return redirect('home')
    else:
        form = UserRegister()

    return render(request, 'student/register.html', {'form': form})



