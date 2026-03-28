from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import UserForm


def index(request):
    tasks = Task.objects.all().order_by('-created')
    return render(request, "tasks/index.html", {"tasks": tasks})


def view_task(request, task_id):  # Добавили task_id
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "tasks/view_task.html", {"task": task})


def create_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST.get("description", "")
        priority = request.POST.get("priority", 1)
        Task.objects.create(title=title, description=description, priority=priority)
        return redirect("index")
    return render(request, "tasks/create_task.html")


def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.title = request.POST["title"]
        task.description = request.POST.get("description", "")
        task.complete = "completed" in request.POST
        task.save()  # Важно вызвать save()!
        return redirect("index")
    return render(request, "tasks/edit_task.html", {"task": task})


def delete_task(request, task_id):  # Добавили task_id
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("index")
    return render(request, "tasks/delete_task.html", {"task": task})


def user_form_view(request):
    if request.method == 'POST':
        userform = UserForm(request.POST, request.FILES)
        if userform.is_valid():
            pass
    else:
        userform = UserForm()

    return render(request, 'tasks/form.html', {'form': userform})
