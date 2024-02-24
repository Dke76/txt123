#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6573695895:AAFVK1IVBmN2egCnVCZBujt4bi3yhPktyFU")
    API_ID = int(os.environ.get("API_ID", "16818625"))
    API_HASH = os.environ.get("API_HASH", "38fb061efb9e27b865f6923d2bb03e49")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1366906399")
