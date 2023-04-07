from ckeditor.fields import RichTextField
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.


class Course(models.Model):
    title = models.CharField(verbose_name="Название курса", max_length=150)
    content = RichTextField(blank=True, null=True)
    preview_image = models.ImageField(
        verbose_name="Фотка для заставки", upload_to="courses/", null=True, blank=True)
    study_duration = models.CharField(
        verbose_name="Длительность обучения", default="", max_length=100)
    students_in_group = models.CharField(
        verbose_name="Количество учеников в группе", max_length=100, default='')
    has_checkbox = models.BooleanField(help_text="Включить, если у описания статьи есть переключение между месяцами",
                                       default=False)
    slug = models.SlugField(
        help_text="Данное поле заполняется само при добавлении названия курса", default="")

    def get_preview_image(self):
        if self.preview_image:
            return self.preview_image.url
        return "https://gurulab.uz/wp-content/uploads/2022/02/course-2-2048x1456.jpg"

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Master(models.Model):
    name = models.CharField(verbose_name="Имя мастера",
                            max_length=150, unique=True)
    content = RichTextField(null=True, blank=True,
                            verbose_name="Описание мастера")
    photo = models.ImageField(verbose_name="Фото мастера", upload_to="photos/masters/", null=True, blank=True,
                              default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"


class NewItem(models.Model):
    """Модель новости"""
    title = models.CharField(verbose_name="Название новости", max_length=350)
    short_descr = RichTextField(verbose_name="Короткое описание новости", default="")
    content = RichTextField(verbose_name="Полное описание новости")
    image = models.ImageField(verbose_name="Фото новости")
    created_at = models.DateTimeField(verbose_name="Дата создания статьи")
    slug = models.SlugField(verbose_name="Название новости на латинице", null=True, blank=True, max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["pk"]
