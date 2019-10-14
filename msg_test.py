# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta
from weixin.login import WeixinLogin
from weixin import WeixinMP, WeixinError
from weixin import WeixinMsg

APPID = "wx54c21c8a4904255d"
APPSECRET = "971f6efee4663d9c19cbd08ba323dbc0"
TEMPLATEID = "WcX2LSm7MyMBEUQZPGM2MEof_oXBIOn_jMJeQmLRpOs"

mp = WeixinMP(APPID, APPSECRET)

def send_template_message(template_id, openid, data, url):
    response = None
    if url == None:
        response = mp.template_send(template_id, openid, data)
    else:
        response = mp.template_send(template_id, openid, data, url)
    return response

template_data = data = {
    "from_address": {
        "value": "古城广陵"
    },
    "sn": {
        "value": "252765166851"
    },
    "sign_time": {
        "value": "2019-01-15 10:41:32"
    },
    "tip": {
        "value": "对快递员的服务还满意吗？ 点击详情，给TA一个评价吧！还可查看快递员和运单详情。",
        "color": "#FF0000"
    }
}

send_template_message(TEMPLATEID, "ogFPewVmsL9wVuf6yIzINVCS7ykY", template_data, None)