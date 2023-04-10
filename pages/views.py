from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Master, Course, NewItem


# Create your views here.
def index_view(request):
    masters = Master.objects.all()
    courses = Course.objects.all()[:4]
    images = [f"images/index_more/{i}.webp" for i in range(1, 20) if i not in (9, 10, 11)]

    context = {
        "masters": masters,
        "courses": courses,
        "images": images
    }
    return render(request, "pages/index.html", context)


def courses_view(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, "pages/courses.html", context)


def course_detail(request, slug):
    course = Course.objects.filter(slug=slug).first()
    courses = Course.objects.all()
    context = {
        "course": course,
        "courses": courses
    }
    return render(request, "pages/course_detail.html", context)


def news_view(request):
    news = NewItem.objects.all()
    paginator = Paginator(news, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }
    return render(request, "pages/news.html", context)


def news_detail(request, slug):
    new_item = NewItem.objects.filter(slug=slug).first()
    context = {
        "new": new_item
    }
    return render(request, "pages/news_detail.html", context)
