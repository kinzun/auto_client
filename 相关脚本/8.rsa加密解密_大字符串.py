#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
pip3 install rsa
asdf
"""
import rsa
import base64
 

# ######### 1. 生成公钥私钥 #########
pub_key_obj, priv_key_obj = rsa.newkeys(1024) # 128 - 11 = 117
# 公钥字符串
pub_key_str = pub_key_obj.save_pkcs1()
pub_key_code = base64.standard_b64encode(pub_key_str)
print(pub_key_code)
# 私钥字符串
priv_key_str = priv_key_obj.save_pkcs1()
priv_key_code = base64.standard_b64encode(priv_key_str)
print(priv_key_code)

#
# # # ######### 2. 加密 #########
def encrypt(pub_key_code,value):
    key_str = base64.standard_b64decode(pub_key_code)
    pk = rsa.PublicKey.load_pkcs1(key_str)
    value_bytes = value.encode('utf-8')
    data_list = []
    for i in range(0,len(value_bytes),117):
        chunk = value_bytes[i:i+117]
        result = rsa.encrypt(chunk, pk)
        data_list.append(result)

    return b''.join(data_list)


data = encrypt(pub_key_code,'zff'*1000)
print(len(data),data)
#
# # ######### 3. 解密 #########

def decrypt(priv_key_code,bytes_value):
    key_str = base64.standard_b64decode(priv_key_code)
    pk = rsa.PrivateKey.load_pkcs1(key_str)
    result = []
    for i in range(0,len(bytes_value),128):
        chunk = bytes_value[i:i+128]
        val = rsa.decrypt(chunk, pk)
        result.append(val)
    return b''.join(result)

origin = decrypt(priv_key_code,data)
origin_str = origin.decode('utf-8')
print(origin_str)


#
# # ######### 基本使用 #########
# if __name__ == '__main__':
#     v = 'wupeiqi'
#     v1 = encrypt(v)
#     print(v1)
#     v2 = decrypt(v1)
#     print(v2)