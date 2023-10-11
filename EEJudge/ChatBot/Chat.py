# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/11
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import random
import time

def respond(message, chat_history):
    bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
    chat_history.append((message, bot_message))
    time.sleep(2)
    return "", chat_history
