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
response=requests.get(url)
print(response.content)
with open("logo.png","wb") as f:
    f.write(response.content)
    f.close()

#带headers请求
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
response=requests.get("http://www.baidu.com",headers=headers)
print(response.text)

#POST请求
data={
    "name":"john",
    "age":"22"
}
response=requests.post("http://httpbin.org/psot",data=data)
print(response.text)

#POST请求增加headers
response=requests.post("http://httpbin.org/post",data=data,headers=headers)
print(response.json())

#response属性
response=requests.get("http://www.jianshu.com")
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.url),response.url)
print(type(response.history),response.history)

#状态码判断
response=requests.get("http://www.jianshu.com")
exit() if not response.status_code==requests.codes.ok else print("Requests Successfully")

exit() if not response.status_code==requests.codes.ok else print("Requests Successfully")

response=requests.get("http://www.jianshu.com/hello.html")
exit() if not response.status_code==requests.codes.not_found else print("404 html page not found")

#文件上传
files={"file":open("logo.png","rb")}
response=requests.post("http://httpbin.org/post",files=files)
print(response.text)

#获取cookie
response=requests.get("http://www.baidu.com")
print(response.cookies)
for key,value in response.cookies.items():
    print(key+"="+value)

#获取cookies,模拟登陆
s=requests.Session()
s.get("http://httpbin.org/cookies/set/number/1234556789")
response=s.get("http://httpbin.org/cookies")
print(response.text)

#超时设置
response=requests.get("https://httpbin.org",timeout=1)
print(response.status_code)

#异常处理
from requests.exceptions import ReadTimeout,HTTPError,RequestException
try:
    response=requests.get("http://httpbin.org/get",timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print("timeout")
except HTTPError:
    print("http error")
except RequestException:
    print("error")