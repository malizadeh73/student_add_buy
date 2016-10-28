#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ApiApp.handlers.main_handler import add_buy_Handler


url_patterns = [
    ("/add_buy", add_buy_Handler, None, "add_buy"),
]
