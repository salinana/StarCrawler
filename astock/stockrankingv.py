from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
options.add_argument('--blink-settings=imagesEnabled=false')
the_file = open('stocklistv.txt', 'r')
lines = the_file.readlines()
the_file.close()
start_num = 5000
end_num = 6000

while True:
    try:
        driver = webdriver.Chrome(options=options)
        count=0
        for line in lines[start_num:end_num]:
            t = time.localtime()
            current_time = time.strftime("%Y%m%d_%H:%M:%S", t)

            line=line.replace("\n","")
            driver.get("http://guba.eastmoney.com/rank/stock?code="+line)
            time.sleep(0.25)
            ranknum=driver.find_element(By.CSS_SELECTOR,"span[class='ranknum']").text
            count = count + 1
            print(str(count)+" "+line+"_"+current_time+"-->"+ranknum)
        driver.quit()
    except:
        driver.quit()