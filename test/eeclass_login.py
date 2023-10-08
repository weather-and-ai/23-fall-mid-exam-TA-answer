# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/07
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import sys
from os.path import join
from os.path import dirname
from os.path import abspath

project_root = join(
    dirname(abspath(__file__)),
    '..',
)
sys.path.append(project_root)

from EEJudge.Login import Bot
import aiohttp
import asyncio
from dotenv import dotenv_values

async def main():
    async with aiohttp.ClientSession() as session:

        config = dotenv_values(".env")
        bot = Bot(
            session=session,
            account=config["account"],
            password=config["password"],
        )
        await bot.login()

if __name__ == '__main__':
    asyncio.run(main())
