# -*- coding: utf-8 -*-
import requests
response=requests.get("https://www.baidu.com")
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
#带参数的get请求
data={
    'name':'geemey',
    'age':22
}
response=requests.get("http://httpbin.org/get",params=data)
print(response.text)
#把返回结果转码成JSON
import json
response=requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))

#获取二进制数据
url="https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png"
response=requests.get(url,headers=headers)
print(response.content)
with open("logo.png","wb") as f:
    f.write(response.content)
    f.close()

#带headers请求
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
response=requests.get("http://www.baidu.com",headers=headers)
print(response.text)