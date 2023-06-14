from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def loginPage(request):
    return render(request, 'lmsapp/loginPage.html')


def superAdminPage(request):
    return render(request, 'lmsapp/superAdminHP.html')


def index(request):

    return render(request, 'lmsapp/index.html')


def about(request):
    return render(request, 'lmsapp/about.html')


def course(request):
    tasks = Task.objects.all()
    return render(request, 'lmsapp/course.html', {'title': 'Main Page Of Site', 'tasks': tasks})


def price(request):
    return render(request, 'lmsapp/price.html')


def addCourse(request):
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course')
        else:
            eror = "Error"

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'lmsapp/addCourse.html', context)

