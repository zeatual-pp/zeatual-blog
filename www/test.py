# -*- coding: utf-8 -*-

import orm
from models import User,Blog,Comment
import asyncio

async def test(loop):
    await orm.create_pool(loop=loop,user='zeatual',password='password',db='zeatualblog')
    u=User(name='bincheng',email='zzzzzzs@163.com',passwd='333aifubaba3',image='about:blank')

    await u.save()
    # await User.findAll()

loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop))
print('test','success')
loop.close()