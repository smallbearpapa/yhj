#!/usr/bin/python
#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
soup=BeautifulSoup("<html><p><!-- TEXT --></></html>","html.parser")
print(type(soup.p.string))