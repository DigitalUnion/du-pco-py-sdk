"""
 * @Author: gaojian
 * @Description: A simple way to call DigitalUnion service
 * @Date: 2022/11/04 14:28 PM
"""
import zlib

from dupco import aes


def encode(data, key):
    """
    The key argument should be the AES key, should be 16 bytes
    :param data: string
    :param key: string
    :return: bytes
    """
    compress_byte = zlib.compress(data.encode())
    return aes.encrypt(compress_byte, key)


def decode(data, key):
    """
    The key argument should be the AES key, should be 16 bytes
    :param data: bytes/bytearray/memoryview
    :param key: string
    :return: Returns a bytes object containing the uncompressed data.
    """
    decrypt_data = aes.decrypt(data, key)
    return zlib.decompress(decrypt_data)
