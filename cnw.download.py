from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import urllib.request


file=open('urls/cn.woman.txt', 'r')
lines=file.readlines()
count = 0
# Strips the newline character
for line in lines:
    count += 1
    print(count)
    words=str(line).split('|')
    print(words[0])
    print(words[1])
    print(words[2])
    print(words[3])
    index=words[0]
    name=words[1]
    url=words[3]
    if not os.path.isdir("images/cnw/"+index+name):
        os.makedirs("images/cnw/"+index+name)
    if not os.path.exists("images/cnw/"+index+name+"/"+index+name+".jpeg"):
        urllib.request.urlretrieve(url, "images/cnw/"+index+name+"/"+index+name+".jpeg")

