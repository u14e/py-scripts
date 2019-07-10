# @Author: u14e
# @Time  : 2019/6/27 10:51
# @description: 入口程序
import logging

logging.basicConfig(level=logging.DEBUG)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def index(request):
    await asyncio.sleep(0.5)
    return web.json_response({
        'name': 'index'
    })

def run():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host='0.0.0.0', port=8010)

if __name__ == '__main__':
    run()
