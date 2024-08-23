from tortoise.contrib.fastapi import register_tortoise
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import LastNews
from fastapi import FastAPI, Query
from fastapi import Request
from parse import *
import uvicorn


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")





@app.get("/")
async def index(request: Request):
    news_list = await LastNews.all()
    return templates.TemplateResponse("index.html", {
      "request": request,
      "news_list": news_list
    })

register_tortoise(
    app,
    db_url="sqlite://news.db",
    modules={"models": ["main"]},
    add_exception_handlers=True,
    generate_schemas=True
)


@app.get("/about_us/")
def about_us(request: Request):
  return templates.TemplateResponse("about_us.html", {"request": request})


@app.get("/help/")
def help(request: Request):
  return templates.TemplateResponse("help.html", {"request": request})


# News List Container
@app.get("/news/")
def news(request: Request):
  news_list = get_news()
  return templates.TemplateResponse("news.html", {
    "request": request,
    "news_list": news_list,
  })


@app.get("/news-war/")
def news_war(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_war_list, total_pages = get_news_war(page, page_size)

  return templates.TemplateResponse("news-war.html", {
    "request": request,
    "news_war_list": news_war_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })





@app.get("/news-ukraine/")
def news_ukraine(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_ukraine_list, total_pages = get_news_ukraine(page, page_size)
  return templates.TemplateResponse("news-ukraine.html", {
    "request": request,
    "news_ukraine_list": news_ukraine_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })



@app.get("/news-politics/")
def news_politics(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_politics_list, total_pages = get_news_politics(page, page_size)
  return templates.TemplateResponse("news-politics.html", {
    "request": request,
    "news_politics_list": news_politics_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-world/")
def news_world(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_world_list, total_pages = get_news_world(page, page_size)
  return templates.TemplateResponse("news-world.html", {
    "request": request,
    "news_world_list": news_world_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })



@app.get("/news-ecology/")
def news_ecology(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_ecology_list, total_pages = get_news_ecology(page, page_size)
  return templates.TemplateResponse("news-ecology.html", {
    "request": request,
    "news_ecology_list": news_ecology_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-insurance/")
def news_insurance(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_insurance_list, total_pages = get_news_insurance(page, page_size)
  return templates.TemplateResponse("news-insurance.html", {
    "request": request,
    "news_insurance_list": news_insurance_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-covid/")
def news_covid(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_covid_list, total_pages = get_news_covid(page, page_size)
  return templates.TemplateResponse("news-covid.html", {
    "request": request,
    "news_covid_list": news_covid_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-weapon/")
def news_weapon(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_weapon_list, total_pages = get_news_weapon(page, page_size)
  return templates.TemplateResponse("news-weapon.html", {
    "request": request,
    "news_weapon_list": news_weapon_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-science/")
def news_science(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_science_list, total_pages = get_news_science(page, page_size)
  return templates.TemplateResponse("news-science.html", {
    "request": request,
    "news_science_list": news_science_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-technology/")
def news_technology(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_technology_list, total_pages = get_news_technology(page, page_size)
  return templates.TemplateResponse("news-technology.html", {
    "request": request,
    "news_technology_list": news_technology_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-health/")
def news_health(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_health_list, total_pages = get_news_health(page, page_size)
  return templates.TemplateResponse("news-health.html", {
    "request": request,
    "news_health_list": news_health_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-kyiv/")
def news_kyiv(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_kyiv_list, total_pages = get_news_kyiv(page, page_size)
  return templates.TemplateResponse("news-kyiv.html", {
    "request": request,
    "news_kyiv_list": news_kyiv_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-lviv/")
def news_lviv(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_lviv_list, total_pages = get_news_lviv(page, page_size)
  return templates.TemplateResponse("news-lviv.html", {
    "request": request,
    "news_lviv_list": news_lviv_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-dnipro/")
def news_dnipro(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_dnipro_list, total_pages = get_news_dnipro(page, page_size)
  return templates.TemplateResponse("news-dnipro.html", {
    "request": request,
    "news_dnipro_list": news_dnipro_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-harkov/")
def news_harkov(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_harkov_list, total_pages = get_news_harkov(page, page_size)
  return templates.TemplateResponse("news-harkov.html", {
    "request": request,
    "news_harkov_list": news_harkov_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-odessa/")
def news_odessa(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_odessa_list, total_pages = get_news_odessa(page, page_size)
  return templates.TemplateResponse("news-odessa.html", {
    "request": request,
    "news_odessa_list": news_odessa_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })


@app.get("/news-attractions/")
def news_attractions(request: Request, page: int = Query(1, alias='page', ge=1), page_size: int = Query(7, alias='size', ge=1)):
  news_attractions_list, total_pages = get_news_attractions(page, page_size)
  return templates.TemplateResponse("news-attractions.html", {
    "request": request,
    "news_attractions_list": news_attractions_list,
    "current_page": page,
    "total_pages": total_pages,
    "page_size": page_size,
  })



if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", reload=True)