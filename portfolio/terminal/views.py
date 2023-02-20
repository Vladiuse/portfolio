from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import Directory, Poll
from django.template.loader import get_template
from django.template.context import RequestContext
from django.template import Template, loader
import time
import os
from django.conf import settings
from .snipets_view import get_templates
from pprint import pprint

DEFAULT_COLOR_THEME = 'blue'
AVAILABLE_COLOR_THEMES = [DEFAULT_COLOR_THEME, 'purple', 'green']
START_PAGE_FILE_ID = 'terminal/files/about_page.html'


def index(request):
    color_theme = request.COOKIES.get('color_theme')
    if color_theme not in AVAILABLE_COLOR_THEMES:
        color_theme = DEFAULT_COLOR_THEME
    nodes = Directory.objects.all()
    start_file_id = START_PAGE_FILE_ID
    DIRS = get_templates(to_json=False)
    content = {
        'nodes': nodes,
        'start_file_id': start_file_id,
        'color_theme': color_theme,
        'DIRS': DIRS,
    }
    return render(request, 'terminal/index.html', content)


def test(request):
    poll = Poll.objects.get(pk=1)
    content = {
        'poll': poll,
    }
    return render(request, 'terminal/test.html', content)


def get_file_content(request):
    file_id = request.GET['file_id']
    print(file_id, 'xxxxx')
    content = loader.render_to_string(file_id, {}, request)
    time.sleep(0.5)
    result = {
        'status': True,
        'content': content,
    }
    return JsonResponse(result, safe=True)
