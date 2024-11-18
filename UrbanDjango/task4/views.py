from django.shortcuts import render
from lib2to3.fixes.fix_input import context
from django.template.context_processors import request
from django.views.generic import TemplateView


def home(request):
    title = 'Cайт Django'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/home.html', context)


def shop(request):
    title = 'Cайт Django'
    text = 'Магазин игр'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/shop.html', context)


def cart(request):
    title = 'Cайт Django'
    text_h1 = 'Корзина'
    text = 'Извините ваша корзина пуста'
    context = {
        'title': title,
        'text_h1': text_h1,
        'text': text,
    }
    return render(request, 'fourth_task/cart.html', context)

# Create your views here.
