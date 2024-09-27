import requests
from bs4 import BeautifulSoup
import sys
import time
counter =0
linkListesi=[]
#encoding
sys.stdout.reconfigure(encoding='utf-8')
r = requests.get("https://www.amazon.com.tr/gp/bestsellers?ref_=nav_cs_bestsellers")
#wait for page to load
time.sleep(4)
soup = BeautifulSoup(r.content, "lxml")
ürünler = soup.find_all("li", attrs = {"class":"a-carousel-card"})
for ürün in ürünler:
  ürün_linkleri = ürün.find_all("a", attrs={"class":"aok-block"})
  for link in ürün_linkleri:
    counter+=1
    linkinÖnü="https://www.amazon.com.tr/"
    ürün_linki_devam = link.get("href")
    stringDonustur=str(ürün_linki_devam)
    linkinÖnü+=stringDonustur
    linkListesi.append(linkinÖnü)
for link in linkListesi:
  print(link)
print(counter)
