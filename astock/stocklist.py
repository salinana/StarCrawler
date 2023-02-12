from selenium import webdriver
import time
from selenium.webdriver.common.by import By

the_file=open('stocklist.txt', 'w')
driver = webdriver.Chrome()
driver.get("http://quote.eastmoney.com/center/gridlist.html#hs_a_board")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"th[aria-label='代码']").click()
time.sleep(1)
elements=driver.find_elements(By.CSS_SELECTOR,"tr[class='odd'],tr[class='even']")
print(elements[0].text)
for ele in elements:
    list=ele.text.split(' ')
    code=list[1]
    print(code)
    the_file.write(code+"\n")

for pageindex in range(2,266):
    driver.find_element(By.CSS_SELECTOR,"a[class='next paginate_button']").click()
    time.sleep(2)
    elements = driver.find_elements(By.CSS_SELECTOR, "tr[class='odd'],tr[class='even']")
    print(elements[0].text)
    for ele in elements:
        list = ele.text.split(' ')
        code = list[1]
        print(code)
        the_file.write(code + "\n")

