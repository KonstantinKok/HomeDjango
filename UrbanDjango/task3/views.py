from django.shortcuts import render
from lib2to3.fixes.fix_input import context
from django.template.context_processors import request
from django.views.generic import TemplateView

def home(request):
    title= 'Cайт Django'
    text= 'Главная страница'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/home.html', context)


def shop(request):
    title= 'Магазин'
    text= 'Магазин игр'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/shop.html', context)

def cart(request):
    title = 'Корзина'
    text = 'Извините корзина пуста'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/cart.html', context)

# Create your views here.
