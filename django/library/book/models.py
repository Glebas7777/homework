from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    age = models.IntegerField(verbose_name="Возраст")

    def __str__(self):
        return f"{self.pk} - {self.first_name[0]}.{self.last_name}"


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name="Авторы")

    def __str__(self):
        return f"{self.pk} - {self.name}"

