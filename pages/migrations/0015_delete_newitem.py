# Generated by Django 4.1.7 on 2023-04-02 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0014_alter_newitem_slug"),
    ]

    operations = [
        migrations.DeleteModel(
            name="NewItem",
        ),
    ]