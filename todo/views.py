from django.shortcuts import render,redirect
from .models import R_Task
# Create your views here.

def home(request):
    tasks=R_Task.objects.filter(is_completed=False).order_by('updated_at')
    context={
        'tasks':tasks
    }
    return render(request,'home.html',context)

def addtask(request):
    tasks=request.POST['task']
    R_Task.objects.create(task=tasks)
    return redirect("home")

def edittask(request,pk):
    return render(request,'edittask.html')