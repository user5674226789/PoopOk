from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Ви успішно увійшли в акаунт")

                return redirect(reverse('app_name:function-name'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'PoopOk - Авторизація',
        'form': form
    }
    return render(request, 'app_name:function-name', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)

    else:
        form = UserRegistrationForm()
    context = {
        'title': 'PoopOk - Реєстрація',
        'form': form
    }
    return render(request, 'app_name:function-name', context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Ви вийшли з акаунту")
    auth.logout(request)
    return redirect(reverse('app_name:function-name'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Оновлення пройшло успішно")
            return redirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'PoopOk - Кабінет',
        'form': form,
    }
    return render(request, 'app_name:function-name', context)
