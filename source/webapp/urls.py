from django.urls import path
from webapp.views import IndexView, TodolistView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todolist/<int:pk>', TodolistView.as_view(), name='todolist_view'),
    path('add/', CreateView().as_view(), name='todolist_add'),
    path('delete/<int:pk>', DeleteView().as_view(), name='todolist_delete_view'),
    path('update/<int:pk>', UpdateView().as_view(), name='todolist_update_view')

]
