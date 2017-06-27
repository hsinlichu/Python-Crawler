#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import requests
import sys
from bs4 import BeautifulSoup

res=requests.get("https://tw.search.bid.yahoo.com/search/auction/product?qt=product&kw=iphone+7+plus&p=iphone+7+plus")

print("---------------------------------------------")
soup=BeautifulSoup(res.text)
print("---------------------------------------------")
#print(soup.text)

for i in soup.select(".contentwrap"): 
    print(i.select("em"))
    print(i.select("em")[0].text,i.select(".srp-pdtitle a")[0].text)



