import json
import os

import requests

from gurulab import settings
# from pages.models import NewItem

NEWS_IMAGES_FOLDER = os.path.join(settings.MEDIA_ROOT, "photos", "news")


def read_json(file_name: str):
    with open(file_name, mode="r", encoding="utf-8") as file:
        return json.load(file)


def save_news_images(filename):
    data = read_json(filename)
    for i in data:
        for item in data[i]:
            img = item["preview_img"].split("/")[-1]
            res = requests.get(item["preview_img"]).content
            with open(f"{settings.MEDIA_ROOT}\\{img}", mode="wb") as file:
                file.write(res)
            print("Добавили фотку", img)

# save_news_images("../gurulab-news.json")


def change_img_in_news_items():
    res = []

    for f, a, images in os.walk(settings.MEDIA_ROOT):
        if f == settings.MEDIA_ROOT:
            for idx, image in enumerate(images):
                res.append((idx, image))

    return res


