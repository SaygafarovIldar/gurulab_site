from django.core.management.base import BaseCommand

from helpers.main import change_img_in_news_items
from pages.models import NewItem


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        images = change_img_in_news_items()
        for idx, image in images:
            obj = NewItem.objects.filter(pk=idx).first()

            if not obj:
                continue

            obj.image = image
            obj.save()
            print(obj)

