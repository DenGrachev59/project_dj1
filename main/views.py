from django.shortcuts import render

from main.models import Student


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f'{name}, ({email}) сообщение:/{message}/')

    context = {
        'title': 'Контакты',
        'description': 'контактная информация и форма обратной связи',
    }

    return render(request, 'main/contact.html', context)


def index(request):
    students_list = Student.objects.all()
    context = {
        'object_list': students_list,
        'title': 'Главная',
        'description': 'описание главной страницы',
    }

    return render(request, 'main/index.html', context)
