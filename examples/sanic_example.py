from sanic import Sanic
from sanic.response import text, json

app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request):
    return json({'message': 'Hello World'})


# def foo(n: int) -> str:
#     return str(n ** 2)
