import requests
from bs4 import BeautifulSoup

# Новини дня
def get_news():
  response = requests.get("https://hromadske.ua/news")
  if response.status_code != 200:
    raise Exception("Failed to fetch news, status code: {}".format(response.status_code))

  soup = BeautifulSoup(response.content, "html.parser")
  headers = soup.select('.l-feed-list .c-feed-item')

  result = []
  base_url = "https://hromadske.ua"

  for news in headers:
    time = news.select_one(".c-feed-item__time").text.strip()
    title = news.select_one("a > h3").text.strip()
    url = base_url + news.select_one("a")['href']

    news_obj = {
      "time": time,
      "title": title,
      "url": url,
    }
    result.append(news_obj)
  return result




# Війна
def get_news_war(page: int = 1, page_size: int = 7):
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

  # Пагінація
  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages


# Україна
def get_news_ukraine(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages


# Політика
def get_news_politics(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages


# Світ
def get_news_world(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages


# Екологія
def get_news_ecology(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages


# Страхування
def get_news_insurance(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages


# Коронавірус
def get_news_covid(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages


# Зброя
def get_news_weapon(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages


# Наука
def get_news_science(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages



# Технології
def get_news_technology(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages


# Здоров'я
def get_news_health(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages



# Київ
def get_news_kyiv(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages



# Львів
def get_news_lviv(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages



# Дніпро
def get_news_dnipro(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages



# Харків
def get_news_harkov(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages



# Одеса
def get_news_odessa(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages



# Цікавинки
def get_news_attractions(page: int = 1, page_size: int = 7):
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

  start = (page - 1) * page_size
  end = start + page_size
  paginated_result = result[start:end]

  total_pages = (len(result) + page_size - 1) // page_size

  return paginated_result, total_pages