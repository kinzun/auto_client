#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
pip3 install rsa
asdf
"""
import rsa
import base64

# ######### 1. 生成公钥私钥 #########
# 1024 位的证书，加密时最大支持117个字节，解密时为128；
# 2048 位的证书，加密时最大支持245个字节，解密时为256。
pub_key_obj, priv_key_obj = rsa.newkeys(2048)  # 128 - 11 = 117
# 公钥字符串
pub_key_str = pub_key_obj.save_pkcs1()
pub_key_code = base64.standard_b64encode(pub_key_str)
print(pub_key_code)
# 私钥字符串
priv_key_str = priv_key_obj.save_pkcs1()
priv_key_code = base64.standard_b64encode(priv_key_str)
print(priv_key_code)


# # ######### 2. 加密 #########
def encrypt(pub_key_code, value):
    key_str = base64.standard_b64decode(pub_key_code)
    pk = rsa.PublicKey.load_pkcs1(key_str)
    result = rsa.encrypt(value.encode('utf-8'), pk)
    return result


data = encrypt(pub_key_code, 'zff')
print(len(data), data)


# # ######### 3. 解密 #########
def decrypt(priv_key_code, value):
    key_str = base64.standard_b64decode(priv_key_code)
    pk = rsa.PrivateKey.load_pkcs1(key_str)
    val = rsa.decrypt(value, pk)
    return val


origin = decrypt(priv_key_code, data)
print(origin)
#
# # ######### 基本使用 #########
# if __name__ == '__main__':
#     v = 'wupeiqi'
#     v1 = encrypt(v)
#     print(v1)
#     v2 = decrypt(v1)
#     print(v2)
