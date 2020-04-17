from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add/', addToDo, name='add'),
    path('complete/<todo_id>/', completeToDo, name='complete'),
    path('deletecomplete/', deleteCompleted, name='deletecomplete'),
    path('deleteall', deleteAll, name='deleteAll'),
]
