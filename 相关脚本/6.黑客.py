#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests


ret = requests.post(
    # url='http://127.0.0.1:8000/api/test/?sign=41ac0aa7c01a58806fb4149fae689c52&ctime=1540023488278'
    # url='http://127.0.0.1:8000/api/test/?sign=8eb87a62e08407e98d2b95ff3543f287&ctime=1540024002471'
    url='http://127.0.0.1:8000/api/test/?sign=41ac0aa7c01a58806fb4149fae689c52&ctime=1540024643558'
)
print(ret.text)