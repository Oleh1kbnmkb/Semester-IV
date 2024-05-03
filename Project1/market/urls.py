from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
  # path('', views.register, name='register.html'),
  path('', views.index, name='index.html'),
  path('about', views.about, name='about.html'),
  path('contact', views.contact, name='contact.html'),
  path('about_me', views.about_me, name='about_me.html'),
  # path('login', views.login, name='login.html'),
  path('register_user/', views.register_user, name='register_user.html'),
  path('add_product', views.admin_page, name='admin.html'),
]

urlpatterns += staticfiles_urlpatterns()

