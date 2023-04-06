from django.contrib import admin

from .models import Course, Master, NewItem
from modeltranslation.admin import TranslationAdmin

# Register your models here.


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    list_display = ("pk", "title", "slug")
    list_display_links = ("pk", "title")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(NewItem)
class NewItemAdmin(TranslationAdmin):
    """Отображения админки для модели новости"""
    list_display = ("pk", "title", "slug")
    list_display_links = ("pk", "title")

    prepopulated_fields = {"slug": ("title",)}


@admin.register(Master)
class MasterAdmin(TranslationAdmin):
    list_display = ("pk", "name")
    list_display_links = ("pk", "name")




