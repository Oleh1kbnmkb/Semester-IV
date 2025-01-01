from fastapi import FastAPI, HTTPException
from pydantic import HttpUrl
import httpx
from bs4 import BeautifulSoup
import uvicorn

app = FastAPI()



async def fetch_page(url: str) -> str:
  async with httpx.AsyncClient() as client:
    response = await client.get(url)
    if response.status_code != 200:
      raise HTTPException(status_code=response.status_code, detail="Error fetching the webpage")
    return response.text


@app.post("/parse/")
async def parse_page(url: HttpUrl):
  html_content = await fetch_page(str(url))
  soup = BeautifulSoup(html_content, "html.parser")
  title = soup.title.string if soup.title else "No title found"
  links = [a['href'] for a in soup.find_all('a', href=True)][:10]

  return {
    "title": title,
    "links": links
  }



@app.get("/parse/")
async def get_parsed_data(url: HttpUrl):
  html_content = await fetch_page(str(url))
  soup = BeautifulSoup(html_content, "html.parser")

  data = {}
  developer = soup.find("th", text="Developer")
  if developer:
    data["Developer"] = developer.find_next_sibling("td").text.strip()

  os = soup.find("th", text="Operating system")
  if os:
    data["OS"] = os.find_next_sibling("td").text.strip()

  license_info = soup.find("th", text="License")
  if license_info:
    data["License"] = license_info.find_next_sibling("td").text.strip()

  return data


if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", reload=True)