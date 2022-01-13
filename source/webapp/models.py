from django.db import models

# Create your models here.


class Todolist(models.Model):
    summary = models.CharField(max_length=2000, null=True, blank=False, verbose_name="Кратеое Описание")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Полное описание")
    status = models.ForeignKey('webapp.Status', related_name='tasks', verbose_name="Статус", on_delete=models.PROTECT)
    type = models.ForeignKey('webapp.Type', related_name='tasks', verbose_name='Тип', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f'{self.pk}. {self.summary} {self.status}'

    class Meta:
        db_table = 'to_do_list'
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'


class Status(models.Model):
    status = models.CharField(max_length=100, null=False, blank=False, verbose_name='Статус')

    def __str__(self):
        return f'{self.pk}. {self.status}'

    class Meta:
        db_table = 'Status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    type = models.CharField(max_length=100, null=False, blank=False, verbose_name='Тип')

    def __str__(self):
        return f'{self.pk}. {self.type}'

    class Meta:
        db_table = 'Type'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

