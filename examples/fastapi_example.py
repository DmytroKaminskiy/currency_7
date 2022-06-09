# asgi
from fastapi import FastAPI
import httpx

app = FastAPI()

URLS = [
   'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
   'https://uk.wikipedia.org/wiki/%D0%92%D1%96%D0%BA%D1%96%D0%BF%D0%B5%D0%B4%D1%96%D1%8F:%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB_%D1%81%D0%BF%D1%96%D0%BB%D1%8C%D0%BD%D0%BE%D1%82%D0%B8',
   'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D1%96_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B8',
   'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:LintErrors',
]


async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.status_code



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/get-many')
async def hello_world():
    url = URLS[0]
    status_code = await fetch_url(url)
    return {'message': status_code}
