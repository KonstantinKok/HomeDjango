from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    users = ['Konstantin']

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username in users and password == repeat_password and int(age) > 18:
            return HttpResponse(f'Приветствуем, {username}!')

        elif username in users:
             return HttpResponse(f'Имя {username} - занято. Выберите другое имя')

        elif password != repeat_password:
             return HttpResponse(f'{username}, Пароли не совпадают!!!')

        elif int(age) < 18:
             return HttpResponse(f'{username}, Вам нет 18!!!')

    return render(request, "task5/registration_page.html")

# Create your views here.
