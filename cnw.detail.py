from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
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
    url=words[2]


    if not os.path.isdir("profiles/cnw/"+index+name):
        os.makedirs("profiles/cnw/"+index+name)

    if os.path.exists("profiles/cnw/"+index+name+"/"+index+name+".txt"):
        pfile = open("profiles/cnw/"+index+name+"/"+index+name+".txt", 'r')
        plines=pfile.readlines()
        if len(plines)==0:
            os.remove("profiles/cnw/"+index+name+"/"+index+name+".txt")

    if not os.path.exists("profiles/cnw/"+index+name+"/"+index+name+".txt"):
        while True:
            try:
                driver.get(url)
                break
            except Exception:
                continue

        time.sleep(2)
        if "您所访问的页面不存在" in str(driver.page_source):
            continue

        nameList=driver.find_elements(By.CSS_SELECTOR,"dt[class='basicInfo-item name']")
        if nameList is None:
            continue
        valueList=driver.find_elements(By.CSS_SELECTOR,"dd[class='basicInfo-item value']")
        pfile = open("profiles/cnw/" + index + name + "/" + index + name + ".txt", 'w')
        for name,value in zip(nameList,valueList):
            print(name.text.replace(" ",""),value.text.strip().replace("\n",""))
            pfile.write(name.text.replace(" ","")+":"+value.text.strip().replace("\n","")+"\n")
        try:
            visitSpan=driver.find_element(By.CSS_SELECTOR,"span[id='j-lemmaStatistics-pv']")
            print("浏览次数:"+visitSpan.text.strip()+"\n")
            pfile.write("浏览次数:"+visitSpan.text.strip()+"\n")
            summaryDiv=driver.find_element(By.CSS_SELECTOR,"div[class='lemma-summary']")
            print("简介:" +summaryDiv.text.replace("\n",""))
            pfile.write("简介:" + summaryDiv.text.replace("\n",""))
        except Exception:
            continue0