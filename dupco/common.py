import base64
import zlib

from dupco import aes


def encode(data, key):
    compress_byte = zlib.compress(data.encode())
    return aes.encrypt(compress_byte, key)


def decode(data, key):
    decrypt_data = aes.decrypt(data, key)
    return zlib.decompress(decrypt_data)
