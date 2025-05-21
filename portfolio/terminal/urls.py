from django.urls import path

from . import views

app_name = "terminal"
urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),
    path("get_file_content", views.get_file_content, name="file_content"),
]
