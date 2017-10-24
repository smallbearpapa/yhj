# -*- coding: utf-8 -*-
import re
#match方法
content="hello 123 4567 world_this is a Regex Demo"
result=re.match(r"^hello\s\d{3}\s\d{4}\s\w{10}.*Demo$",content)
print(len(content))
print(result)
print(result.group())
print(result.span())

result=re.match(r"^hello.*Demo$",content)
print(len(content))
print(result)
print(result.group())
print(result.span())
#匹配目标
result=re.match(r"^hello\s(\d+)\s.*Demo$",content)
print(len(content))
print(result)
print(result.group(1))
print(result.span())
#贪婪匹配
result=re.match(r"^he.*(\d+)\s.*Demo$",content)
print(result.group(1))
#非贪婪匹配
result=re.match(r"^he.*?(\d+)\s.*Demo$",content)
print(result.group(1))
#匹配模式,设置re.s，.匹配换行符
content='''hello 123 4567 world_this
 is a Regex
 Demo'''
result=re.match(r"^he.*?(\d+)\s.*Demo$",content,re.S)
print(result.group(1))
#转义
content="price is $5.00"
result=re.match("price is \$5\.00",content)
print(result)

#为匹配方便，能用search就不用match
content="Extra strings Hello 1234567 World_This is a Regex Demo Extra strings"
result=re.search("Hello\s(\d+).*?Demo",content)
print(result.group(1))

html='''<div id="songs-list>
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
    <li data-view="2">一路上有你</li>
    <li data-view="7">
    <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
    </li>
    <li data-view="4" class="active">
    <a href="/3.mp3" singer="齐秦">往事随风</a>
    </li>
    <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
    <li data-view="5"><a href="/5.mp3" singer="陈慧林">记事本</a></li>
    <li data-view="5">
    <a href="/3.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
    </li>
    </ul>
<div>'''
result=re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result.group(1),result.group(2))
#findall方法
results=re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(results)
for result in results:
    print(result)

results=re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
print(results)

content="Extra strings Hello 1234567 World_This is a Regex Demo Extra strings"
#content=re.sub("\d+","",content)
#content=re.sub("\d+","Replacement",content)
content=re.sub("(\d+)",r"\1 8910",content)
print(content)
html=re.sub("<i.*?></i>","",html)
print(html)
html=re.sub("<a.*?>|</a>","",html)
print(html)
results=re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
print(results)
content='''Hello 1234567 World_This
is a Regex Demo
'''
pattern=re.compile('Hello.*?Demo',re.S)
result=re.match(pattern,content)
print(result)
#实战练习
import requests
content=requests.get("https://book.douban.com").text
print(content)
pattern=re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?author.*?>(.*?)</div>.*?</li>',re.S)
results=re.findall(pattern,content)
print(results)