"""
 * @Author: gaojian
 * @Description: A simple way to call DigitalUnion service
 * @Date: 2022/11/04 14:28 PM
"""
import json

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
OTHER_ERROR_CODE = 10999

sdk_ver = "v1.1.2"


class Client(object):
    def __init__(self, client_id, secret_key, secret_val, domain):
        self.__client_id = client_id
        self.__secret_key = secret_key
        self.__secret_val = secret_val
        self.__domain = domain

    def call(self, api_id, data):
        headers = {
            CLIENT_ID: self.__client_id,
            SECRET_KEY: self.__secret_key,
            API_ID_KEY: api_id,
            SDK_VER_KEY: sdk_ver,
        }
        result = {"code": 0}
        try:
            if len(data) != 0:
                data = common.encode(data, self.__secret_val)
            resp = post(self.__domain, data, headers=headers)
        except Exception as e:
            result["code"] = OTHER_ERROR_CODE
            result["msg"] = str(e)
            return result
        if resp.status_code >= 400:
            result["code"] = OTHER_ERROR_CODE
            result["msg"] = FMT_HTTP_CODE_ERROR % resp.status_code
            return result
        if resp.status_code == 200:
            try:
                result_byte = common.decode(resp.content, self.__secret_val)
                result = json.loads(result_byte)
                return result
            except Exception as e:
                result["code"] = OTHER_ERROR_CODE
                result["msg"] = str(e)
                return result

    @staticmethod
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
