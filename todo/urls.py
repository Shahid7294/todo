from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("addtask/",views.addtask,name='addtask'),
    path("Mark_as_Done/<int:pk>/",views.Mark_as_Done,name='Mark_as_Done'),
    path("Mark_as_UnDone/<int:pk>/",views.Mark_as_UnDone,name='Mark_as_UnDone'),
    path("edittask/<int:pk>/",views.edittask,name='edittask'),
    path("del/<int:pk>/",views.del_task,name='del_task')
]
