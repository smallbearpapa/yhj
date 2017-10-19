# -*- coding: utf-8 -*-
import requests
#不带headers请求
response=requests.get(r"http://www.baidu.com")
print(response.text)
print(response.status_code)
#带headers请求
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
response=requests.get("http://www.baidu.com",headers=headers)
print(response.text)
print(response.status_code)
#下载图片
url="https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png"
response=requests.get(url,headers=headers)
print(response.content)
with open("logo.png","wb") as f:
    f.write(response.content)
    f.close()