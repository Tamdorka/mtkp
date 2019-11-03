from main.models import *
from main.forms import *

from django.urls import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from django.db import IntegrityError

from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from itertools import chain
# Create your views here.

def search_id_link(id_link):
    """
        Функция ищет пользователя с id_link, возвращает его.
        В случае неудачи возвращает page404.
    """
    lst = list(chain(Student.objects.all(), Teacher.objects.all()))
    for item in lst:
        if item.id_link == id_link:
            return item
    
    raise Http404

def get_base_context(request):
    """
        Возвращает стандартный набор контекстного словаря.
    """
    context = {
        'user': request.user,
    }
    return context

# Simple viewing pages
def index_page(request):
    context = get_base_context(request)
    context['title'] = 'Главная страница'
    context['main_header'] = 'Главная страница'
    return render(request, 'pages/index.html', context)

# Student user handling
def register_page(request):
    context = get_base_context(request)
    context['title'] = 'Регистрация'
    context['main_header'] = 'Регистрация пользователя'
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateStudentForm(request.POST)
            if form.is_valid():
                student = form.save()
                login(request, student.user)
                return redirect('/accounts/user/')

            context['user_creation_form'] = form
        else:
            context['user_creation_form'] = CreateStudentForm()
    else:
        return redirect('/index.html')
    return render(request, 'pages/accounts/register.html', context)

def login_page(request):
    context = get_base_context(request)
    context['title'] = 'Вход на сайт'
    context['main_header'] = 'Войти на сайт'
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginUserForm(request.POST)
            if form.is_valid():
                if form.user_login(request):
                    return redirect('/')
            context['user_signin_form'] = form
        else:
            context['user_signin_form'] = LoginUserForm()
    else:
        return redirect('/accounts/user/')
    return render(request, 'pages/accounts/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('/')

def profile_page(request, id_link=None):
    context = get_base_context(request)
    context['title'] = 'Профиль'
    context['main_header'] = 'Страница пользователя'
    
    if id_link is not None:
        query = search_id_link(id_link)
    else:
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/accounts/sign_in/')
    
    return render(request, 'pages/accounts/user.html', context)

# Overwriting error pages to templates/errors/...
def handler404(request, exception=''):
    context = get_base_context(request)
    context['title'] = 'Не найдено'
    context['main_header'] = '404, Не найдено!'
    return render(request, 'errors/404.html', context, status=404)

def handler500(request, exception=''):
    context = get_base_context(request)
    context['title'] = 'Ошибка сервера'
    context['main_header'] = '500, На сервере что-то пошло не так!'
    return render(request, 'errors/500.html', context, status=500)

def handler400(request, exception=''):
    context = get_base_context(request)
    context['title'] = 'Неправильный запрос'
    context['main_header'] = '400, Что-то не так с запросом!'
    return render(request, 'errors/400.html', context, status=400)

def handler403(request, exception=''):
    context = get_base_context(request)
    context['title'] = 'Ошибка просмотра'
    context['main_header'] = '403, Кажется у вас нет прав на просмотр!'
    return render(request, 'errors/403.html', context, status=403)
