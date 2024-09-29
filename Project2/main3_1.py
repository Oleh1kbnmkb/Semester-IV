import httpx
from pprint import pprint

# url = ""
urls = ["https://goiteens.com/course/minecraft/",
        "https://goiteens.com/mini-courses/",
        "https://goiteens.com/club/",
        "https://goiteens.com/free/",
        "https://goiteens.com/blog/"]

try:
    for url in urls:
        with httpx.Client() as client:
            response = client.get(url)
            print("Headers:")
            pprint(dict(response.headers)['cache-control'])
            pprint(dict(response.headers)['cache-control'])
except Exception as e:
    print(f"An error occurred: {e}")
