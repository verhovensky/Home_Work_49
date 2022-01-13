from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView

from webapp.forms import TodolistForm
from webapp.models import Todolist
# Create your views here.


class IndexView(View):


    def todolist_view(self, request, *args, **kwargs):
        todolist = Todolist.objects.order_by("deadline")
        return render(request, 'index.html', {'todolist': todolist})


def create_todolist_view(request):
    if request.method == 'GET':
        form = TodolistForm()
        return render(request, 'create_todolist.html', {'form': form})
    else:
        form = TodolistForm(data=request.POST)
        if form.is_valid():
            summary = form.cleaned_data.get('summary')
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')
            new_todolist = Todolist.objects.objects.create(summary=summary, description=description, status=status, type=type)
            return redirect('todolist_view', pk=new_todolist)
        return render(request, 'create_todolist.html', {'form': form})


class TodolistView(TemplateView):

    def get_context_data(self, **kwargs):
        description = super().get_context_data(**kwargs)
        todolist = get_object_or_404(Todolist, pk=kwargs.get('pk'))
        description['todolist'] = todolist
        return description


def todolist_update_view(request, pk):
    todolist = get_object_or_404(Todolist, pl=pk)
    if request.method == 'GET':
        form = TodolistForm(initial={
            'summary': todolist.summary,
            'todolist': todolist.todolist,
            'description': todolist.description,
            'status': todolist.status,
            'type': todolist.type
        })
        return render(request, 'todolist_update.html', {'todolist': todolist, 'form': form})
    else:
        form = TodolistForm(data=request.POST)
        if form.is_valid():
            todolist.summary = request.POST.get('summary')
            todolist.description = request.POST.get('description')
            todolist.status = request.POST.get('status')
            todolist.type = request.POST.get('type')
            todolist.save()
            return redirect('todolist_view', pk=todolist.pk)
    return render(request, 'todolist_update.html', {'todolist': todolist, 'form': form})


def todolist_delete_view(request, pk):
    todolist = get_object_or_404(Todolist, pk=pk)
    if request.method == 'GET':
        return render(request, 'todolist_delete.html', {'todolist': todolist})
    else:
        todolist.delete()
        return redirect('index')