# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

async def index(request):
    return web.Response(text='初步搭建框架！')

app=web.Application()
app.add_routes([web.get('/',index)])
web.run_app(app,host='127.0.0.1',port=9090)

