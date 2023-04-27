import sys
from django.db import models

from users.models import CustomUser
from django import forms


sys.path.insert(0, '/fawn_files/home')


class Files(models.Model):
    title = models.CharField('Название', max_length=128)
    anons = models.CharField('Анонс', max_length=250)
    url = models.URLField('URL файла для загрузки', max_length=120)
    slug = models.SlugField('URL', unique=True, db_index=True)
    full_txt = models.TextField('Полное описание')
    datetime = models.DateTimeField('Дата публикации', auto_now_add=True)
    version = models.ManyToManyField('Version', blank=False, related_name='files')
    type = models.ForeignKey('Type', on_delete=models.PROTECT, null=True, related_name='files')
    favourite = models.ManyToManyField(CustomUser, default=None, blank=True, related_name='favourite')
    creator = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, related_name='files')
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class Comment(models.Model):
    file = models.ForeignKey(Files, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField('Текст')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.body}:{self.file.pk}:{self.user}'


class Version(models.Model):
    name = models.CharField('Название', max_length=40, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


class Type(models.Model):
    name = models.CharField('Название', max_length=40, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
