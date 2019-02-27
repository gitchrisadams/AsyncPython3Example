
import asyncio
import aiohttp
import requests

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = response.content()
    print('{}: {} bytes'.format(url, len(data)))
    return data

futures = [call_url(url) for url in urls]

# .run is not compatible with python 3.5, Maybe python 3.7?
#asyncio.run(asyncio.wait(futures))
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
loop.close()