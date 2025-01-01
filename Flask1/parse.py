import requests
from bs4 import BeautifulSoup

# Новини дня
def get_news():
  response = requests.get("https://hromadske.ua/news")
  soup = BeautifulSoup(response.content, "html.parser")
  result = []
  all_urls = soup.select(".l-feed-list .c-feed-item > a")
  default_img_url = "https://ksoe.com.ua/assets/ed3d37a5/5cf0de66aa9f4.jpg"

  for a_tag in all_urls:
    url = a_tag['href']
    request = requests.get(url)
    page_soup = BeautifulSoup(request.content, "html.parser")

    title = page_soup.select_one(".c-heading__title").text.strip()
    img_tag = page_soup.select_one(".c-post-image__picture.c-post-image__picture > img")
    desc = page_soup.select_one(".o-lead > p")
    desc_text = desc.text.strip() if desc else "No description available"

    # Обмеження кількості символів для description до 229
    if len(desc_text) > 229:
      desc_text = desc_text[:229]  # Обрізаємо текст до 229 символів

    time_tag = page_soup.select_one(".c-post-header__date")
    if time_tag:
      time_text = time_tag.text.strip()
      time_only = time_text[-5:]
    else:
      time_only = "No time available"

    if img_tag and 'src' in img_tag.attrs:
      img_url = img_tag['src']
      if not img_url.startswith("http"):
        img_url = "https://hromadske.ua" + img_url  # Додаємо домен, якщо URL відносний
    else:
      img_url = default_img_url

    news_obj = {
      "time": time_only,
      "title": title,
      "url": url,
      "description": desc_text,
      "image_url": img_url
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



def get_inter():
  response = requests.get("https://ua.korrespondent.net/interview/")
  soup = BeautifulSoup(response.content, "html.parser")
  result = []

  headers = soup.select('.unit-rubric .article.article_rubric_top')

  for inter in headers[:7]:
    title = inter.select_one(".article__title").text.strip()
    url = inter.select_one("a")['href']
    img_tag = inter.select_one(".article__img-link > img")
    img_url = (
      img_tag.get('data-src') or
      img_tag.get('data-href') or
      img_tag.get('src') if img_tag else None
    )

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url
    }
    result.append(news_obj)

  return result


def get_plot():
  response = requests.get("https://ua.korrespondent.net/special/1657-suizhety")
  soup = BeautifulSoup(response.content, "html.parser")
  result = []

  headers = soup.select('.articles-list .article.article_rubric_top')

  for plot in headers[:5]:
    title = plot.select_one(".article__title > h3").text.strip()
    url = plot.select_one("a")['href']
    img_tag = plot.select_one(".article__img-link > img")
    img_url = (
      img_tag.get('data-src') or
      img_tag.get('data-href') or
      img_tag.get('src') if img_tag else None
    )

    news_obj = {
      "img_url": img_url,
      "title": title,
      "url": url
    }
    result.append(news_obj)

  return result