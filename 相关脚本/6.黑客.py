import requests
import hashlib
from config import settings
import time


def gen_sign(ctime):
    """
    生成URL签名
    :param ctime:
    :return:
    """
    val = '%s|%s' % (settings.URL_AUTH_KEY, ctime,)
    obj = hashlib.md5()
    obj.update(val.encode('utf-8'))
    return obj.hexdigest()


ctime = int(time.time() * 1000)

url = f'http://127.0.0.1:8000/api/asset/?sign={gen_sign(ctime)}&ctime={ctime}'

ret = requests.post(
    url='http://127.0.0.1:8000/api/test/?sign=41ac0aa7c01a58806fb4149fae689c52&ctime=1540023488278'
    # url=url,
    # url='http://127.0.0.1:8000/api/test/?sign=41ac0aa7c01a58806fb4149fae689c52&ctime=1540024643558'
)
print(url)
print(ret.text)
print(ret.json())
