# Django
from django.urls import path
from django.views.generic import TemplateView

# Local
from . import views

urlpatterns = [
    # Root
    path('', views.index, name='index',),

    path('about/', TemplateView.as_view(template_name='app/about.html'), name='about',),
    path('privacy/', TemplateView.as_view(template_name='app/privacy.html'), name='privacy',),
    path('support/', TemplateView.as_view(template_name='app/support.html'), name='support',),


    # Authentication
    path('login', views.login, name='login'),
    path('callback', views.callback, name='callback'),
    path('logout', views.logout, name='logout'),

    # Dashboard
    path('dashboard', views.dashboard, name='dashboard',),

]
