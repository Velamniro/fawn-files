from django.contrib import admin
from .models import *


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('user', 'body')
    list_display = ('body', 'file', 'created_on')
    list_filter = ('created_on',)


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    search_fields = ('title', 'full_txt')
    prepopulated_fields = {"slug": ('title',)}
    list_display = ("title", "anons",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ("name", "id",)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ("name", "id",)

