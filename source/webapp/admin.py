from django.contrib import admin

# Register your models here.

from models import Todolist


class TodolistAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'status', 'deadline']
    list_filter = ['status']
    search_fields = ['task', 'deadline']
    fields = ['task', 'status', 'deadline', 'description']


admin.site.register(Todolist, TodolistAdmin)