# @Author: u14e
# @Time  : 2019/6/27 10:21
# @description: https://www.liaoxuefeng.com/wiki/1016959663602400/1017985577429536
import asyncio
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