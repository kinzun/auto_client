# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from sys import path

base_path = path.append(os.path.dirname(os.path.dirname(__file__)))

from src.script import run

if __name__ == '__main__':
    run()
