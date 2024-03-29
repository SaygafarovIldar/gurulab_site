# Generated by Django 4.1.7 on 2023-04-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0016_newitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newitem",
            name="image",
            field=models.ImageField(
                upload_to="photos/news/", verbose_name="Фото новости"
            ),
        ),
        migrations.AlterField(
            model_name="newitem",
            name="title",
            field=models.CharField(max_length=350, verbose_name="Название новости"),
        ),
    ]
