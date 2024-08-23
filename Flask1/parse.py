import requests
from bs4 import BeautifulSoup

# Новини дня
def get_news():
  response = requests.get("https://hromadske.ua/news")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.l-feed-list .c-feed-item')
  result = []

  for news in headers:
    time = news.select_one(".c-feed-item__time").text
    title = news.select_one("a > h3").text
    url = news.select_one("a")['href']

    news_obj = {
      "time": time,
      "title": title,
      "url": url,
    }
    result.append(news_obj)

  return result




# Війна
def get_news_war():
  response = requests.get("https://www.unian.ua/war")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result


# Україна
def get_news_ukraine():
  response = requests.get("https://www.unian.ua/society")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result


# Політика
def get_news_politics():
  response = requests.get("https://www.unian.ua/politics")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result


# Світ
def get_news_world():
  response = requests.get("https://www.unian.ua/world")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result


# Екологія
def get_news_ecology():
  response = requests.get("https://www.unian.ua/ecology")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result


# Страхування
def get_news_insurance():
  response = requests.get("https://www.unian.ua/insurance")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result


# Коронавірус
def get_news_covid():
  response = requests.get("https://covid.unian.ua/")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result


# Зброя
def get_news_weapon():
  response = requests.get("https://www.unian.ua/weapons")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result


# Наука
def get_news_science():
  response = requests.get("https://www.unian.ua/science")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result



# Технології
def get_news_technology():
  response = requests.get("https://www.unian.ua/techno")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result


# Здоров'я
def get_news_health():
  response = requests.get("https://www.unian.ua/health")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result



# Київ
def get_news_kyiv():
  response = requests.get("https://www.unian.ua/kyiv")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result



# Львів
def get_news_lviv():
  response = requests.get("https://www.unian.ua/lvov")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result



# Дніпро
def get_news_dnipro():
  response = requests.get("https://www.unian.ua/dnepropetrovsk")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result



# Харків
def get_news_harkov():
  response = requests.get("https://www.unian.ua/kharkiv")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result



# Одеса
def get_news_odessa():
  response = requests.get("https://www.unian.ua/odessa")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result



# Цікавинки
def get_news_attractions():
  response = requests.get("https://www.unian.ua/curiosities")
  soup = BeautifulSoup(response.content, "html.parser")

  headers = soup.select('.list-thumbs .list-thumbs__item')
  result = []

  for news in headers:
    img_tag = news.select_one("img")
    img_url = img_tag.get("data-src") or img_tag.get("src")
    title = news.select_one(".list-thumbs__info > h3 > a").text.replace('\n', '')
    url = news.select_one("a")['href']
    time = news.select_one(".list-thumbs__time.time").text

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url,
      "time": time,
    }
    result.append(news_obj)

  return result