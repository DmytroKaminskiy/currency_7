'''
Async - in one thread (IO)
Thread - IO (GIL)
Process - CPU
'''
from time import sleep, time

# def foo():
#     print('Foo Start')
#     sleep(1)
#     print('Foo End')
#
# start = time()
# foo()
# foo()
# foo()
# print(f'Took time: {time() - start}')

# import asyncio
#
# async def foo():
#     print('Foo Start')
#     await asyncio.sleep(1)
#     print('Foo End')
#
# async def main():
#     await asyncio.gather(foo(), foo(), foo())
#
# start = time()
# # event loop
# asyncio.run(main())
# print(f'Took time: {time() - start}')

# yield from
# @coroutine
import asyncio
# import requests
# import httpx as requests
import httpx

# sync 64.9
# async  5.3
async def fetch_url(url):
    # response = requests.get(url)
    # print(response.status_code)

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(response.status_code)


async def main():
    urls = [
               'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
               'https://uk.wikipedia.org/wiki/%D0%92%D1%96%D0%BA%D1%96%D0%BF%D0%B5%D0%B4%D1%96%D1%8F:%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB_%D1%81%D0%BF%D1%96%D0%BB%D1%8C%D0%BD%D0%BE%D1%82%D0%B8',
               'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D1%96_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B8',
               'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:LintErrors',
           ] * 40
    await asyncio.gather(*[fetch_url(url) for url in urls])


start = time()
# event loop
asyncio.run(main())
print(f'Took time: {time() - start}')
# asyncio[client,server], iohttp[client,server]
# sanic