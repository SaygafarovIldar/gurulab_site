# Generated by Django 4.1.7 on 2023-03-30 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0011_newitem"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newitem",
            options={"verbose_name": "Новость", "verbose_name_plural": "Новости"},
        ),
    ]
