from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import R_Task
# Create your views here.

def home(request):
    tasks=R_Task.objects.filter(is_completed=False).order_by('updated_at')
    is_completed=R_Task.objects.filter(is_completed=True)
    context={
        'tasks':tasks,
        'is_completed':is_completed
    }
    return render(request,'home.html',context)

def addtask(request):
    tasks=request.POST['task']
    R_Task.objects.create(task=tasks)
    return redirect("home")
def Mark_as_Done(request,pk):
    task=get_object_or_404(R_Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def Mark_as_UnDone(request,pk):
    task=R_Task.objects.get(pk=pk)
    # task=get_object_or_404(R_Task,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

def edittask(request,pk):
    get_task=R_Task.objects.get(pk=pk)
    if request.method == "POST":
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task':get_task
        }
        return render(request,'edittask.html',context)
    
def del_task(request,pk):
    task=R_Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')
