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
    path('settings', views.settings, name='settings'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
    path('update_prod/<arrivals_id>', views.update_prod, name='update_prod'),
    path('delete_prod/<arrivals_id>', views.delete_prod, name='delete_prod'),
    path('add_to_basket/<product_id>', views.add_to_basket, name='add_to_basket'),
    path('view_basket', views.view_basket, name='view_basket'),
]


urlpatterns += staticfiles_urlpatterns()


