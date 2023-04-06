from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name="index"),
    path("news/", views.news_view, name="news"),
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),
    path("courses/", views.courses_view, name="courses"),
    path("courses/<slug:slug>/", views.course_detail, name="course_detail"),
]
