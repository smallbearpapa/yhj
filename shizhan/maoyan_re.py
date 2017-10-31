# -*- coding: utf-8 -*-
import requests
from requests.exceptions import RequestException
from multiprocessing import Pool
import re
import json

def get_one_page(url):
    try:
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        else:
            return None
    except RequestException:
        return None
def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">'
                       '<a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)'
                       '</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    results=re.findall(pattern,html)
    for result in results:
        yield {
            "index":result[0],
            "image":result[1],
            "title":result[2],
            "actor":result[3].strip()[3:],
            "time":result[4].strip()[5:],
            "score":result[5]+result[6]
        }
def write_to_file(content):
    with open("maoyan.txt","a",encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+"\n")
        f.close()
def main(offset):
    url="http://maoyan.com/board/4?offset="+str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
       print(item)
       write_to_file(item)

if __name__=="__main__":
    pool=Pool()
    pool.map(main,[i*10 for i in range(10)])