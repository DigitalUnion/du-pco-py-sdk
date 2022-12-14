"""
 * @Author: gaojian
 * @Description: A simple way to call DigitalUnion service
 * @Date: 2022/11/04 14:28 PM
"""
from Crypto.Cipher import AES


def encrypt(data, secret_key):
    secret_key = fill_key(secret_key)
    block = AES.block_size
    text = pkcs5_padding(data, block)
    cbc = AES.new(secret_key.encode('utf-8'), AES.MODE_CBC, secret_key.encode('utf-8'))
    return cbc.encrypt(text)


def pkcs5_padding(s, block):
    pad_len = block - len(s) % block
    return s + (bytes([pad_len]) * pad_len)


def un_pad(s):
    return s[:-ord(s[len(s) - 1:])]


def decrypt(data, secret_key):
    secret_key = fill_key(secret_key)
    cbc = AES.new(secret_key.encode(), AES.MODE_CBC, secret_key.encode())
    return un_pad(cbc.decrypt(data))


def fill_n(s, count):
    l = len(s)
    c = count // l
    m = count % l
    result = ""
    for i in range(c):
        result += s
    if m != 0:
        result += s[:m]
    return result


def fill_key(key):
    l = len(key)
    if l == 16:
        return key
    if l < 16:
        return fill_n(key, 16)
    return key[:16]
