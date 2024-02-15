from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import lower
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import StudentForm
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


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    # fields = ('first_name', 'last_name', 'avatar', 'is_active')
    success_url = reverse_lazy('main:student_list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    # fields = ('first_name', 'last_name', 'avatar', 'is_active')
    success_url = reverse_lazy('main:student_list')


class StudentListView(ListView):
    model = Student


# def index(request):
#     students_list = Student.objects.all()
#     context = {
#         'object_list': students_list,
#         'title': 'Главная',
#         'description': 'описание главной страницы',
#     }
#
#     return render(request, 'main/student_list.html', context)


class StudentDetailView(DetailView):
    model = Student
    # template_name = 'main/student_detail.html'

# def view_student(request, pk):
#     student_item = get_object_or_404(Student, pk=pk)
#     context = {
#         'object': student_item,
#         'title': 'Информация о студенте ',
#         'description': f'{student_item.first_name} {student_item.last_name}',
#     }
#     return render (request, 'main/student_detail.html', context)

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:student_list')

def toggel_activity(request, pk): #реализация активации/деактивации студента
    student_item= get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse('main:student_list'))