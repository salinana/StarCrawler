from selenium import webdriver
import threading
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import logging
from logging.handlers import RotatingFileHandler
import redis

logging.basicConfig(filename='output.log', level=logging.INFO)
logFile = 'output.log'
my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024,
                                 backupCount=2, encoding='UTF-8', delay=0)
my_handler.setLevel(logging.INFO)
app_log = logging.getLogger('root')
app_log.setLevel(logging.INFO)
app_log.addHandler(my_handler)

redis_host="r-wz9qit3ps7fouiiqhv.redis.rds.aliyuncs.com"
redis_port=6379
redis_password="Kuangbiao123456"
my_redis=redis.Redis(host=redis_host,port=redis_port,password=redis_password)
logging.info("Connected to redis via "+redis_host)

options = Options()
options.headless = True
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument("--no-sandbox") #for unbuntu,it must be set

the_file = open('stocklistv.txt', 'r')
lines = the_file.readlines()
the_file.close()

def getRank(threadname,start_num,end_num):
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
                if ranknum=="-":
                    driver.get("http://guba.eastmoney.com/rank/stock?code=" + line)
                    time.sleep(0.25)
                    ranknum = driver.find_element(By.CSS_SELECTOR, "span[class='ranknum']").text
                count = count + 1
                #print(threadname+" "+str(count)+" "+line+"_"+current_time+"-->"+ranknum)
                key = line + "_" + current_time
                value = ranknum
                my_redis.set(key, value)
                logging.info(threadname+" "+str(count)+" "+line+"_"+current_time+"-->"+ranknum)

            driver.quit()
        except:
            driver.quit()
            continue
# Create two threads as follows
try:
    thread1= threading.Thread(target=getRank,args=["thread1",0,250])
    thread1.start()
    thread2= threading.Thread(target=getRank,args=["thread2",250,500])
    thread2.start()
except:
    logging.info("Error: unable to start thread")

while 1:
   pass