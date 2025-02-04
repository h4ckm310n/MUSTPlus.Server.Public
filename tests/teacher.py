import hashlib
import time

import requests

TOKEN = 'dd974dd0-89c5-11e9-9405-be63b5b3b608'
AUTH_SECRET = r'flw4\-t94!09tesldfgio30'


def calc_sign(get_data: dict, post_data: dict) -> dict:
    get = ''
    for e in sorted(get_data):
        get = get + e + '=' + str(get_data[e]) + '&'
    get = get[:-1]

    post = ''
    for e in sorted(post_data):
        post = post + e + "=" + str(post_data[e]) + "&"
    post = post[:-1]

    params = get + post + AUTH_SECRET
    return hashlib.md5(params.encode('utf-8')).hexdigest()


def teacher(name_zh):
    get_data = {
        'token': TOKEN,
        'time': int(time.time()),
    }
    get_data['sign'] = calc_sign(get_data, {})
    r = requests.get("http://mp.junyi.pw:8000/teacher/" +
                     name_zh, params=get_data)
    return r.text


print(teacher("羅少龍"))
