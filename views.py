from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse


def index(request):
    return render(request, 'chat/index.html')


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            return render(request, 'chat/index.html', {'new_user': new_user})
    else:
        user_form = RegisterForm()
    return render(request, 'chat/registers.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'chat/index.html')
            else:
                return HttpResponse('Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'chat/login.html', {'form': form})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })




