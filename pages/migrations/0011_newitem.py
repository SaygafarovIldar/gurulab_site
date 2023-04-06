# Generated by Django 4.1.7 on 2023-03-30 20:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0010_course_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Название новости"),
                ),
                (
                    "content",
                    ckeditor.fields.RichTextField(verbose_name="Описание новости"),
                ),
                ("image", models.ImageField(upload_to="", verbose_name="Фото новости")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания статьи"
                    ),
                ),
                ("slug", models.SlugField(verbose_name="Название новости на латинице")),
            ],
        ),
    ]