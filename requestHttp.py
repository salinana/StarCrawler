import requests
import sys

x = requests.get('http://baike.baidu.com/item/%E9%BB%84%E5%AD%90%E9%9F%AC/5217042')
print(x.status_code)
print(x.text)