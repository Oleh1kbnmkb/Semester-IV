from aiohttp import web


async def handle(request):
    return web.Response(text="Hello, aiohttp!")


async def handle2(request):
    return web.Response(text="Hello, aiohttp2!")


async def handle3(request):
    return web.Response(text="Hello, aiohttp3!")


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/2', handle)
app.router.add_get('/3', handle)

web.run_app(app, host='127.0.0.1', port=8080)
