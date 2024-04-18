from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
  path('', views.index, name='index.html'),
  path('about', views.about, name='about.html'),
  path('contact', views.contact, name='contact.html'),
  path('about_me', views.about_me, name='about_me.html'),
  path('sign_up', views.sign_up, name='sign_up.html'),
]

urlpatterns += staticfiles_urlpatterns()

