from django.db import models

# Create your models here.

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Todolist(models.Model):
    todolist = models.CharField(max_length=400, null=False, blank=False, verbose_name='Цель')
    status = models.CharField(max_length=30, null=False, blank=False, default='active', choices=status_choices,
                              verbose_name='Статус')
    description = models.TextField(max_length=2000, null=True, blank=False, default="Подробное описание отсутствует",
                                   verbose_name="Описание")
    deadline = models.DateField(null=True, blank=True, default=None, verbose_name="Дата когда задача выполнена")

    def __str__(self):
        return f"{self.pk}.  {self.todolist}: {self.status} / {self.deadline}"

    class Meta:
        db_table = 'to_do_list'
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'