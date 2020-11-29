# Django
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


# Root
def index(request):
    return render(
        request,
        'app/index.html',
    )

def robots(request):
    rendered = render_to_string(
        'robots.txt',
    )
    return HttpResponse(
        rendered,
        content_type="text/plain",
    )

def sitemap(request):
    rendered = render_to_string(
        'sitemap.txt',
    )
    return HttpResponse(
        rendered,
        content_type="text/plain",
    )
