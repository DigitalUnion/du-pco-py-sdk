"""
 * @Author: gaojian
 * @Description: A simple way to call DigitalUnion service
 * @Date: 2022/11/04 14:28 PM
"""
import base64
import http

from requests import post

from dupco import common

BASE_DOMAIN = "https://data.shuzilm.cn/pco/base/sdk"
DATA_DOMAIN = "https://data.shuzijz.cn/pco/data/sdk"
SDK_VER_FOR_TEST = "test"

API_ID_KEY = "api_id"
CLIENT_ID = "client_id"
SECRET_KEY = "secret_key"
SDK_VER_KEY = "sdk_ver"
FMT_HTTP_CODE_ERROR = "HTTP CODE:%d"

sdk_ver = "v1.1.2"


class Client(object):
    def __init__(self, client_id, secret_key, secret_val, domain):
        self.client_id = client_id
        self.secret_key = secret_key
        self.secret_val = secret_val
        self.domain = domain

    def call(self, api_id, data):
        headers = {
            CLIENT_ID: self.client_id,
            SECRET_KEY: self.secret_key,
            API_ID_KEY: api_id,
            SDK_VER_KEY: sdk_ver,
        }
        data = common.encode(data, self.secret_val)
        resp = post(self.domain, data, headers=headers)
        if resp.status_code == 200:
            result = common.decode(resp.content, self.secret_val)
            return result

    @staticmethod
    def enable_test_mode():
        global sdk_ver
        sdk_ver = SDK_VER_FOR_TEST


def enable_test_mode():
    global sdk_ver
    sdk_ver = SDK_VER_FOR_TEST


def new_base_client(client_id, secret_key, secret_val):
    return Client(client_id, secret_key, secret_val, BASE_DOMAIN)


def new_data_client(client_id, secret_key, secret_val):
    return Client(client_id, secret_key, secret_val, DATA_DOMAIN)


if __name__ == '__main__':
    c = new_data_client("cloud-test", "aa", "yDpDEihpUsF_RyWsCES1H")
    c.enable_test_mode()
    ret = c.call("idmap-query-all", '{"f":"mac,imei","k":"868862032205613","m":"0"}')
    print(ret)
