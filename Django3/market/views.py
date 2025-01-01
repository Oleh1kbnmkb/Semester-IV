from django.shortcuts import render, redirect
from .models import LastNews
from .parse import *
from django.core.paginator import Paginator


def index(request):
  last_news = LastNews.objects.all()

  response = render(request, 'index.html', {
    "last_news": last_news,
  })
  return response



def about_us(request):
  return render(request, 'about_us.html')


def help(request):
  return render(request, 'help.html')




# News List Container
def news(request):
  news_list = get_news()
  return render(request, "news_list/news.html", {"news_list": news_list})



def news_war(request):
    news_war_list = get_news_war()
    news_inter = get_inter()
    news_plot = get_plot()
    paginator = Paginator(news_war_list, 6)
    page = request.GET.get('page')
    paginated_list = paginator.get_page(page)
    return render(request, "news_list/news-war.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_ukraine(request):
  news_ukraine_list = get_news_ukraine()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_ukraine_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)
  return render(request, "news_list/news-ukraine.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_politics(request):
  news_politics_list = get_news_politics()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_politics_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)
  return render(request, "news_list/news-politics.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_world(request):
  news_world_list = get_news_world()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_world_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)
  return render(request, "news_list/news-world.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_ecology(request):
  news_ecology_list = get_news_ecology()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_ecology_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)
  return render(request, "news_list/news-ecology.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_insurance(request):
  news_insurance_list = get_news_insurance()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_insurance_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)

  return render(request, "news_list/news-insurance.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_covid(request):
  news_covid_list = get_news_covid()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_covid_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)
  return render(request, "news_list/news-covid.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_weapon(request):
  news_weapon_list = get_news_weapon()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_weapon_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)

  return render(request, "news_list/news-weapon.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_science(request):
  news_science_list = get_news_science()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_science_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)
  return render(request, "news_list/news-science.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_technology(request):
  news_technology_list = get_news_technology()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_technology_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)

  return render(request,"news_list/news-technology.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
  })




def news_health(request):
  news_health_list = get_news_health()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_health_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)

  return render(request, "news_list/news-health.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_kyiv(request):
  news_kyiv_list = get_news_kyiv()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_kyiv_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)

  return render(request, "news_list/news-kyiv.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_lviv(request):
  news_lviv_list = get_news_lviv()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_lviv_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)

  return render(request, "news_list/news-lviv.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_dnipro(request):
  news_dnipro_list = get_news_dnipro()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_dnipro_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)

  return render(request, "news_list/news-dnipro.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })


def news_harkov(request):
  news_harkov_list = get_news_harkov()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_harkov_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)

  return render(request, "news_list/news-harkov.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_odessa(request):
  news_odessa_list = get_news_odessa()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_odessa_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)

  return render(request, "news_list/news-odessa.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })



def news_attractions(request):
  news_attractions_list = get_news_attractions()
  news_inter = get_inter()
  news_plot = get_plot()
  paginator = Paginator(news_attractions_list, 6)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)

  return render(request, "news_list/news-attractions.html", {
      "paginated_list": paginated_list,
      "news_inter": news_inter,
      "news_plot": news_plot
    })
