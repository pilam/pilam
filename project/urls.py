# Third-Party
from sentry_sdk import last_event_id

# Django
from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import include
from django.urls import path

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('django-rq/', include('django_rq.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
else:
    def handler(request, *args, **argv):
        return render(
            request,
            "app/500.html",
            {
                'sentry_dsn': settings.SENTRY_DSN,
                'sentry_event_id': last_event_id(),
            },
            status=500,
        )
    handler500 = handler
