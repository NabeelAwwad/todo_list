from django.contrib import admin
from .models import TodoList, ToDoItem

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    pass

@admin.register(ToDoItem)
class TodoItemAdmin(admin.ModelAdmin):
    pass

