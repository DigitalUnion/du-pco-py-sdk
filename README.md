# du-pco-py-sdk
数字联盟产品能力输出平台 Python SDK

## Installation

- python versions: 3.6 and greater

- pip install dupco


## Quickstart
- 发送请求
```python
import dupco


def example_client():
    c = dupco.new_data_client("cloud-test", "aa", "yDpDEihpUsF_RyWsCES1H")
    c.enable_test_mode()
    return c.call("idmap-query-all", '{"f":"mac,imei","k":"868862032205613","m":"0"}')


if __name__ == '__main__':
    result = example_client()
    print(result)
```

- 解密推送数据

```python
	import dupco

if __name__ == '__main__':
    raw = "<your raw>"
    secret_val = "<your secret value>"
    dupco.decode(raw, secret_val)
```