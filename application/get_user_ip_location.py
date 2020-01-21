# import urllib.request
import requests
import json
from flask import request
from flask import jsonify


def get_ip():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

def get_location(ip):
    # ip = "134.201.250.155"
    key = "d2dc5611ce62f4aa6b23f5a61dba68ce"

    url = r"http://api.ipstack.com/{}?access_key={}".format(ip,key)

    response = requests.get(url)
    if response.status_code == 200:
        return(json.loads(response.content.decode('utf-8')))
    else:
        return(0)

