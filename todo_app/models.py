from django.db import models
from django.utils import timezone
from django.urls import reverse


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class TodoList(models.Model):
    title = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField(default=one_week_hence)
    creation_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
        return f"{self.title}: due{self.due_date}"

    class Meta:
        ordering = ["due_date"]
