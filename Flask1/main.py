from flask import Flask, render_template, request, redirect, url_for
from parse import *
from datetime import datetime

app = Flask(__name__)



@app.route("/")
def index():
  return render_template("index.html")


@app.route("/about_us/")
def about_us():
  return render_template("about_us.html")


@app.route("/help/")
def help():
  return render_template("help.html")


# News List Container
@app.route("/news/")
def news():
  news_list = get_news()
  return render_template("news_list/news.html", news_list=news_list)


@app.route("/news-war/")
def news_war():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_war_list = get_news_war()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_war_list) + per_page - 1) // per_page
  items_on_page = news_war_list[start:end]
  return render_template("news_list/news-war.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-ukraine/")
def news_ukraine():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_ukraine_list = get_news_ukraine()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_ukraine_list) + per_page - 1) // per_page
  items_on_page = news_ukraine_list[start:end]
  return render_template("news_list/news-ukraine.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-politics/")
def news_politics():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_politics_list = get_news_politics()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_politics_list) + per_page - 1) // per_page
  items_on_page = news_politics_list[start:end]
  return render_template("news_list/news-politics.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-world/")
def news_world():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_world_list = get_news_world()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_world_list) + per_page - 1) // per_page
  items_on_page = news_world_list[start:end]
  return render_template("news_list/news-world.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-ecology/")
def news_ecology():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_ecology_list = get_news_ecology()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_ecology_list) + per_page - 1) // per_page
  items_on_page = news_ecology_list[start:end]
  return render_template("news_list/news-ecology.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-insurance/")
def news_insurance():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_insurance_list = get_news_insurance()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_insurance_list) + per_page - 1) // per_page
  items_on_page = news_insurance_list[start:end]
  return render_template("news_list/news-insurance.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-covid/")
def news_covid():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_covid_list = get_news_covid()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_covid_list) + per_page - 1) // per_page
  items_on_page = news_covid_list[start:end]
  return render_template("news_list/news-covid.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-weapon/")
def news_weapon():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_weapon_list = get_news_weapon()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_weapon_list) + per_page - 1) // per_page
  items_on_page = news_weapon_list[start:end]
  return render_template("news_list/news-weapon.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-science/")
def news_science():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_science_list = get_news_science()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_science_list) + per_page - 1) // per_page
  items_on_page = news_science_list[start:end]
  return render_template("news_list/news-science.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-technology/")
def news_technology():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_technology_list = get_news_technology()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_technology_list) + per_page - 1) // per_page
  items_on_page = news_technology_list[start:end]
  return render_template("news_list/news-technology.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-health/")
def news_health():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_health_list = get_news_health()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_health_list) + per_page - 1) // per_page
  items_on_page = news_health_list[start:end]
  return render_template("news_list/news-health.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-kyiv/")
def news_kyiv():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_kyiv_list = get_news_kyiv()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_kyiv_list) + per_page - 1) // per_page
  items_on_page = news_kyiv_list[start:end]
  return render_template("news_list/news-kyiv.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-lviv/")
def news_lviv():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_lviv_list = get_news_lviv()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_lviv_list) + per_page - 1) // per_page
  items_on_page = news_lviv_list[start:end]
  return render_template("news_list/news-lviv.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-dnipro/")
def news_dnipro():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_dnipro_list = get_news_dnipro()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_dnipro_list) + per_page - 1) // per_page
  items_on_page = news_dnipro_list[start:end]
  return render_template("news_list/news-dnipro.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-harkov/")
def news_harkov():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_harkov_list = get_news_harkov()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_harkov_list) + per_page - 1) // per_page
  items_on_page = news_harkov_list[start:end]
  return render_template("news_list/news-harkov.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-odessa/")
def news_odessa():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_odessa_list = get_news_odessa()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_odessa_list) + per_page - 1) // per_page
  items_on_page = news_odessa_list[start:end]
  return render_template("news_list/news-odessa.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


@app.route("/news-attractions/")
def news_attractions():
  page = request.args.get('page', 1, type=int)
  per_page = 6
  news_attractions_list = get_news_attractions()
  news_inter = get_inter()
  news_plot = get_plot()
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = (len(news_attractions_list) + per_page - 1) // per_page
  items_on_page = news_attractions_list[start:end]
  return render_template("news_list/news-attractions.html", items_on_page=items_on_page,
                         total_pages=total_pages, page=page, news_inter=news_inter, news_plot=news_plot)


app.run(port=60000, debug=True)
