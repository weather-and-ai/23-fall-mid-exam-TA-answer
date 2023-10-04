# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/04
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

from typing import Any
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent

class Bot:
    BASE_URL = "https://ncueeclass.ncu.edu.tw"
    YEAR = 2023
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": UserAgent("chrome")
    }

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __init__(
            self, 
            session, 
            account, 
            password,
        ) -> None:
        self.session = session
        self.account = account
        self.password = password

    async def login(self) -> bool:
        data = {
            "_fmSubmit": "yes",
            "formVer": "3.0",
            "formId": "login_form",
            "next": "/",
            "act": "keep",
            "account": f"{self.account}",
            "password": f"{self.password}",
        }
        login_url = Bot.BASE_URL + "/index/login"
        resp = await self.session.get(
            Bot.BASE_URL
        )
        # get csrf-t code
        # print("get csrf-t code")
        soup = BeautifulSoup(await resp.text(), 'lxml')
        code = soup.select("#csrf-t > div > input[type=hidden]")
        data['csrf-t'] = code[0]['value']
        # print(data['csrf-t'])
        print("login ......")
        result = await self.session.post(
            login_url, 
            data=data
        )
        result = await result.text()
        result = json.loads(result)
        # print(result)
        if result['ret']['status'] == 'true':
            print(f"login successfully!!!\nwelcome {self.account}")

            # dashboard_url = "https://ncueeclass.ncu.edu.tw/dashboard"
            # resp = await self.session.get(dashboard_url)
            # soup = BeautifulSoup(await resp.text(), 'lxml')

            # with open('output.html', 'w', encoding='utf-8') as file:
            #     file.write(str(soup))
            
            # print(soup)

            return True
        else:
            print("wrong password or username")

            return False
