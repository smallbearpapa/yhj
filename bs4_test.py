# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
#print(soup.prettify())
#print(soup.title)
tag=soup.a
print(tag)
name=soup.a.name
print(name)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
print(tag.attrs)
print(tag.attrs['href'])
print(type(tag.attrs))
print(type(tag))
print(soup.a.string)
print(type(soup.p.string))