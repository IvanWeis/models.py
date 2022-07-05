from django.shortcuts import render
from django.http import HttpResponse

from .models import *   # из файла models.py импортируем ВСЕ

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all() # в переменную posts записываем ВСЕ записи таблицы Women
    cats = Category.objects.all()
    return render(request, 'women/index.html', {'cats': cats, 'posts': posts, 'menu': menu, 'title': 'Главная'})

def show_post(request, post_id):
    return HttpResponse(f"<h1>Статьи по категориям</><p>{post_id}</p>")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id) # в переменную posts отфильтрованные записи таблицы Women
    cats = Category.objects.all()
    return render(request, 'women/index.html', {'cats': cats, 'posts': posts, 'menu': menu, 'title': 'Главная'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About'})

def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</><p>{catid}</p>")
