#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import time
import hashlib


def gen_sign(ctime):
    key = '60xXhoPGZ39z'
    val = '%s|%s' %(key,ctime,)

    obj = hashlib.md5()
    obj.update(val.encode('utf-8'))
    return obj.hexdigest()



ctime = int(time.time() * 1000)
result = requests.post(
    url='http://127.0.0.1:8000/api/test/',
    params={'sign':gen_sign(ctime),'ctime':ctime},
    data='adfasdfasdfasdfasdf'
)
print(result.url,result.text)