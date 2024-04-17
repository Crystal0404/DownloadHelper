import json
import os.path
import time
from json import JSONDecodeError

import requests

file_patch = "dh_config.json"
if not os.path.exists(file_patch):
    open(file_patch, "w").close()

try:
    with open(file_patch, "r") as f:
        config = json.load(f)
except JSONDecodeError:
    print("wtf????")

try:
    for name in config:
        while True:
            re = requests.get(config[name])
            if re.status_code == 200:
                with open(name, "wb") as f:
                    f.write(re.content)
                    print(config[name] + "下载成功")
                break
            else:
                print(config[name] + "下载失败, 5s后重试" + " 状态码: " + str(re.status_code))
                time.sleep(5)
except requests.exceptions.MissingSchema:
    print("下载异常")
