# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

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