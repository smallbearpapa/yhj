# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
html='''
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''
#字符串初始化
doc=pq(html)
print(doc("li"))
#URL初始化
doc=pq(url="http://www.baidu.com")
print(doc("head"))
#文件初始化
doc=pq(filename="demo.html")
print(doc("li"))
#基本的CSS选择器
doc=pq(html)
print(doc("#container .list .item-0"))
item=doc("#container .list")
lis=item.find(".item-1")
print(lis)
print(item.children())
print(item.children(".item-0"))
#父元素
item=doc("li")
content=item.parent()
print(content)
print(type(content))

contents=item.parents()
print(contents)
print(type(contents))

contents=item.parents("#container")
print("==================",contents)
print(type(contents))
#获取兄弟元素
li=doc(".list .item-0.active")
print(li.siblings())
print(li.siblings(".active"))
#获取单个元素
li=doc(".list .item-0.active")
print(li)
#获取多个元素
lis=doc("li").items()
print(type(lis))
for li in lis:
    print(li)
#获取属性
a=doc(".list .item-0 a")
print(a.attr("href"))
print(a.attr.href)
#获取文本
print(a.text())
#获取html
print(a.html())
#DOM操作
#addClass removeClass
li=doc(".item-0.active")
print(li)
li.removeClass("active")
print(li)
li.addClass("active")
print(li)
#attr css
li.attr("name","link")
print(li)
li.css("font-size","14px")
print(li)
#remove
html='''
<div class="wrap">
    hello world!
    <p>This is a parapraph.</p>
</div>
'''
doc=pq(html)
wrap=doc(".wrap")
print(wrap.text())
wrap.find("p").remove()
print(wrap.text())
html='''
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''
#伪类选择器
doc=pq(html)
li=doc("li:first-child")
print(li)
li=doc("li:last-child")
print(li)
li=doc("li:nth-child(2)")
print(li)
li=doc("li:gt(2)")
print(li)
li=doc("li:nth-child(2n)")
print(li)
li=doc("li:contains(second)")
print(li)