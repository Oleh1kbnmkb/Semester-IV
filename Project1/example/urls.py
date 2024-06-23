from django.urls import path
from . import views


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('data/', views.DataPageView.as_view(), name='data'),
]


urlpatterns += staticfiles_urlpatterns()

