import logging;

logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web


def index(request):
    return web.Response(body=b"<h1>Hi, there!</h1>", headers={"content-type": "text/html"})


async def index(request):
    return web.Response(body=b'<h1>Awesome<h1>', content_type='text/html')


app = web.Application()
app.add_routes([web.get('/', index)])
web.run_app(app, host='localhost', port=9000)
