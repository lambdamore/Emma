# -*- coding: utf-8 -*-
import top.api
 
req=top.api.MixnickGetRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))
 
req.nick="tbtest001"
try:
    resp= req.getResponse()
    print(resp)
except Exception,e:
    print(e)
