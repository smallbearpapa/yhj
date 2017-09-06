# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
#print(soup.head)
#print(soup.head.contents)
#print(soup.body.contents)
#print(len(soup.body.contents))
'''print(soup.body.contents[1])
for item in soup.body.children:
    print(item)

for item in soup.body.descendants:
    print(item)
    '''
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
print(soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling)

for link in soup.find_all("a"):
    print(link.get('href'))

for tag in soup.find_all(re.compile("b")):
    print(tag.name)

print(soup.find_all("p","course"))
print(soup.find_all(id="link1"))
print(soup.find_all(id="link"))
print(soup.find_all(id=re.compile("link")))
print(soup.find_all(string="Basic Python"))