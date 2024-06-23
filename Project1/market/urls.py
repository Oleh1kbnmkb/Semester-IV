from django.urls import path, include
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.my_login, name='my_login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('index', views.index, name='index'),
    path('about_me', views.about_me, name='about_me'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('add_product', views.add_product, name='add_product'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ad_lists', views.ad_lists, name='ad_lists')
]


urlpatterns += staticfiles_urlpatterns()


