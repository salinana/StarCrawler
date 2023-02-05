from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/s?wd=%E5%85%A8%E9%83%A8%E6%98%8E%E6%98%9F&rsv_spt=1&rsv_iqid=0xcb07224000039768&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&rsv_sug3=17&rsv_sug1=19&rsv_sug7=100")
toolDiv=driver.find_element(By.CSS_SELECTOR,"div[class='main-container_3akgD c-border']")


html=driver.page_source

time.sleep(5)

emptyData="display: block"

while emptyData=="display: block":
    driver.find_element(By.CSS_SELECTOR,"div[aria-label*='台湾']").click();
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,"div[aria-label*='女']").click();
    time.sleep(5)
    emptyData=driver.find_element(By.CSS_SELECTOR,"div[id='emptyData']").get_attribute("style")
    print(emptyData)

the_file=open('urls/tw.woman.txt', 'w')
count=0
print("--------第一页------------")

pageIndex=1
starElements=driver.find_elements(By.CSS_SELECTOR,"a[href*='baike.baidu.com/item/']")
for starE in starElements:
    try:
        starImg=starE.find_element(By.TAG_NAME,"img")
    except Exception:
        continue

    count = count + 1
    print(str(count))
    print(starE.get_attribute("title"))
    print(starE.get_attribute("href"))
    print(starImg.get_attribute("src"))
    line="tww"+str(count)+"|"+starE.get_attribute("title")+"|"+starE.get_attribute("href")+"|"+starImg.get_attribute("src")+"\n"
    print(line)
    the_file.write(line)

# starElements=driver.find_elements(By.CSS_SELECTOR,"p[class='item-main-title_3c-Fh c-font-medium']")
#
#
# for starE in starElements:
#     #print(starE.text)
#     starEA=starE.find_element(By.TAG_NAME,"a")
#     print(starEA.text)
#     print(starEA.get_attribute("href"))

for pageIndex in range(2,1500):
    emptyData = "display: block;"
    while emptyData == "display: block;":
        css="//div[@aria-label='第"+str(pageIndex)+"页']"
        print("-------------------------------------------------------------------------")
        print(css)
        element = driver.find_element(By.XPATH,css)
        #time.sleep(5)
        element.click()
        time.sleep(2)
        emptyData = driver.find_element(By.CSS_SELECTOR, "div[id='emptyData']").get_attribute("style")
        print(emptyData)
        starElements=driver.find_elements(By.CSS_SELECTOR,"a[href*='baike.baidu.com/item/']")
        for starE in starElements:
            try:
                starImg=starE.find_element(By.TAG_NAME,"img")
            except Exception:
                continue

            count = count + 1
            print(str(count))
            print(starE.get_attribute("title"))
            print(starE.get_attribute("href"))
            print(starImg.get_attribute("src"))

            line = "tww"+str(count) + "|" + starE.get_attribute("title") + "|" + starE.get_attribute(
                "href") + "|" + starImg.get_attribute("src") + "\n"

            the_file.write(line)
the_file.close()
driver.quit()