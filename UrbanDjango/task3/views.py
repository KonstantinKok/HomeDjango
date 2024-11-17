from django.shortcuts import render
from lib2to3.fixes.fix_input import context
from django.template.context_processors import request
from django.views.generic import TemplateView

def index_home(request):
    title= 'Cайт Django'
    text= 'Главная страница'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/home.html', context)


def home(request):
    return render(request, 'third_task/home.html')

def shop(request):
    return render(request, 'third_task/shop.html')

def cart(request):
    return render(request, 'third_task/cart.html')

# Create your views here.
