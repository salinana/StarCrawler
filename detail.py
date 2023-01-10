from selenium import webdriver
import time
from selenium.webdriver.common.by import By

file=open('cn.man.txt','r')
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
