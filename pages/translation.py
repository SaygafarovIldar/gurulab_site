from modeltranslation.translator import register, TranslationOptions
from .models import Course, NewItem, Master


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ("title", "content", "study_duration", "students_in_group")


@register(NewItem)
class NewItemTranslationOptions(TranslationOptions):
    fields = ("title", "short_descr", "content")


@register(Master)
class MasterTranslationOptions(TranslationOptions):
    fields = ("name", "content")