import asyncio
from aiohttp import ClientSession


async def get_html(src: str):
    async with ClientSession() as session:  # 异步的with，会执行半截就暂停，执行其他的语句
        async with session.get(src) as res:
            print(res.status)
            return await res.text()


async def main():

    url = await get_html('http://127.0.0.1:9988/12345?age=20&name=curry')
    print(url)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

"""
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
"""
