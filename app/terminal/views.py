import time

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader

from .snipets import get_templates

DEFAULT_COLOR_THEME = "blue"
AVAILABLE_COLOR_THEMES = [DEFAULT_COLOR_THEME, "purple", "green"]
START_PAGE_FILE_ID = "terminal/files/about_page.html"


def index(request):
    color_theme = request.COOKIES.get("color_theme")
    if color_theme not in AVAILABLE_COLOR_THEMES:
        color_theme = DEFAULT_COLOR_THEME
    start_file_id = START_PAGE_FILE_ID
    DIRS = get_templates(to_json=False)
    resume_link = settings.RESUME_LINK
    content = {
        "start_file_id": start_file_id,
        "color_theme": color_theme,
        "DIRS": DIRS,
        "resume_link": resume_link,
    }
    return render(request, "terminal/index.html", content)


def test(request):
    content = {}
    return render(request, "terminal/test.html", content)


def get_file_content(request):
    file_id = request.GET["file_id"]
    content = loader.render_to_string(file_id, {}, request)
    time.sleep(0.5)
    result = {
        "status": True,
        "content": content,
    }
    return JsonResponse(result, safe=True)
