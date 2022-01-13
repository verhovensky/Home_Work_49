from django.contrib import admin

# Register your models here.


from webapp.models import Todolist, Status, Type


class TodolistAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'created_at', 'updated_at']
    list_filter = ['summary']
    search_fields = ['task', 'deadline']
    fields = ['summary', 'status', 'created_at', 'updated_at', 'description']


admin.site.register(Todolist, TodolistAdmin)
admin.site.register(Status),
admin.site.register(Type)