from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(options=options)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

the_file=open('stocklist.txt', 'r')
lines=the_file.readlines()
the_file.close()

new_file=open('stocklistv.txt', 'w')

count=0
for line in lines:

    line=line.replace("\n","")

    driver.get("http://guba.eastmoney.com/rank/stock?code="+line)
    time.sleep(1)
    ranknum=driver.find_element(By.CSS_SELECTOR,"span[class='ranknum']").text
    if ranknum!="-":
        count = count + 1
        new_file.write(line+"\n")
        print(str(count) + ":" + line+"-->"+ranknum)

new_file.close()

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)