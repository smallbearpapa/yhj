# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
html='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's Story</b>
<p class="story">Once upon a time there were three little sister;ande their names were</p>
<a href="http://example.com/elsie" class="sister" id="link1"><!--Else--></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
<a href="http://example.com/tillie class="sister" id="link3">Tillie</a>;
and they lived at the bottom of the well.</p>
<p class="story">.....</p>
'''
soup=BeautifulSoup(html,"lxml")
#格式化代码，自动补齐html代码
print(soup.prettify())
print(soup.title.string)
#标签选择器
print(soup.title)
print(type(soup.title))
print(soup.head)
#输出第一个查找的结果
print(soup.p)
#获取名称
print(soup.title.name)
#获取属性
print(soup.p.attrs['name'])
print(soup.p['name'])
#获取内容
print(soup.p.text)
print(soup.p.b.string)
#嵌套选择
print(soup.head.title.string)
#子节点和子孙节点
print(soup.p.contents)
#子节点迭代器
print(soup.p.children)
for child in soup.p.children:
    print(child)
#获取子孙节点的迭代器
print(soup.body.descendants)
for value in soup.body.descendants:
    print(value)
#获取父节点
print(soup.a.parent)
#获取祖先节点
print(soup.a.parents)
print("祖先节点：")
for value in soup.a.parents:
    print("--------------------------")
    print(value)
#兄弟节点
print(soup.a.next_siblings)
print(soup.a.previous_siblings)
#标准选择器
print(soup.find_all("a"))
print(type(soup.find_all("a")[0]))
#根据属性进行查找
print(soup.find_all(attrs={"class":"sister"}))
print(soup.find_all(attrs={"name":"dromouse"}))
print(soup.find_all(class_="sister"))
#根据文本内容进行选择
print(soup.find_all(text="Tillie"))
#find 查找返回单个元素，查找到的第一个值，find_all返回所有元素
#find_parents() find_parent()
#find_parents()返回后面所有的祖先节点，find_parent()返回直接父节点
#CSS选择器
#通过select()直接传入CSS选择器即可完成选择
print(soup.select("p"))
print(soup.select(".sister"))
#获取属性
for p in soup.select("p"):
    print(p["class"])
    print(p.attrs["class"])
#获取内容
for p in soup.select("p"):
    print(p.get_text())
