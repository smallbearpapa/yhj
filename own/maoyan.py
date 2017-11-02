# -*- coding: utf-8 -*-
import requests
from requests import RequestException
import re

def get_page_html(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        else:
            return None
    except RequestException:
        return None
def main():
    html=get_page_html("http://maoyan.com/board/4?offset=")
    print(html)

if __name__ == '__main__':
    main()