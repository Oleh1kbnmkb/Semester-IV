from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('about_us/', views.about_us, name='about_us'),
    path('help/', views.help, name='help'),
    path('news-war/', views.news_war, name='news_war'),
    path('news-ukraine/', views.news_ukraine, name='news-ukraine'),
    path('news-politics/', views.news_politics, name='news-politics'),
    path('news-world/', views.news_world, name='news-world'),
    path('news-ecology/', views.news_ecology, name='news-ecology'),
    path('news-insurance/', views.news_insurance, name='news-insurance'),
    path('news-covid/', views.news_covid, name='news-covid'),
    path('news-weapon/', views.news_weapon, name='news-weapon'),
    path('news-science/', views.news_science, name='news-science'),
    path('news-technology/', views.news_technology, name='news-technology'),
    path('news-health/', views.news_health, name='news-health'),
    path('news-kyiv/', views.news_kyiv, name='news-kyiv'),
    path('news-lviv/', views.news_lviv, name='news-lviv'),
    path('news-dnipro/', views.news_dnipro, name='news-dnipro'),
    path('news-harkov/', views.news_harkov, name='news-harkov'),
    path('news-odessa/', views.news_odessa, name='news-odessa'),
    path('news-attractions/', views.news_attractions, name='news-attractions'),
]


urlpatterns += staticfiles_urlpatterns()


