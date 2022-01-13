from django.urls import path
from django.views.generic import RedirectView

from webapp.models import Todolist

from webapp.views import (
    create_todolist_view,
    TodolistView,
    todolist_update_view,
    todolist_delete_view, IndexView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todolist/', RedirectView.as_view(pattern_name='index')),
    path('todolist/add', create_todolist_view, name='todolist_add'),
    path('todolist/<int:pk>/', TodolistView.as_view(pattern_name='todolist_view'), name='todolist_view'),
    path('todolist/<int:pk>/update', todolist_update_view, name='todolist_update_view'),
    path('todolist/<int:pk>/delete', todolist_delete_view, name='todolist_delete_view')

]