import locale
from datetime import datetime

from django.core.management.base import BaseCommand

from helpers.main import read_json
from pages.models import NewItem

locale.setlocale(locale.LC_ALL, 'ru_RU')



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = read_json("gurulab-news.json")

        for value_data in data.values():
            for item in value_data:

                obj = NewItem.objects.create(
                    title=item["full_title"],
                    content=item["description"],
                    short_descr=item["short_descr"],
                    image=item["preview_img"],
                    created_at=datetime.strptime(item["date"], '%d %b %Y'),
                )

                obj.save()
                print("Добавили новость: ", item["full_title"])
