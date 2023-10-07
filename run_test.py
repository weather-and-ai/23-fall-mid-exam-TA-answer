# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/07
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

from EEJudge.Login import Bot
import aiohttp
import asyncio
from dotenv import dotenv_values
import os

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
