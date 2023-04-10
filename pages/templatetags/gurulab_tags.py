from django import template
from pages.models import Course


register = template.Library()


@register.simple_tag()
def get_courses():
    courses = Course.objects.all()
    return courses


@register.simple_tag()
def is_news_page(request):
    path = [item for item in request.path.split("/")]
    if "news" in path or "courses" in path:
        return True


@register.simple_tag()
def is_home_page(request):
    path = [item for item in request.path.split("/") if item]

    return len(path) < 2
