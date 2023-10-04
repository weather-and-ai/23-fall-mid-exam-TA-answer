# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/04
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import requests
from bs4 import BeautifulSoup
import json
import config

BASE_URL = "https://ncueeclass.ncu.edu.tw"
LOGIN_URL = BASE_URL + "/index/login"
