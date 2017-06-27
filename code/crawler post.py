#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

payload='{"counts":[{"svc":"NV","guid":"a180a15b-9e4f-4575-b28f-927fcb5c63a3"}]}'          #將它變為字串 然後用header中宣告的json解碼

head={"Content-Type":"application/json"}

res=requests.post("https://www.moneydj.com/InfoSvc/apis/vc", data=payload, headers=head)
print(res.text)


print("---------------------------------------------")
soup=BeautifulSoup(res.text)
print("---------------------------------------------")
#print(soup.text)





