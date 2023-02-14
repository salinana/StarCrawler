import redis
import time

the_file = open('stocklistv.txt', 'r')
codes = the_file.readlines()
the_file.close()

redis_host="kuangbiao.redis.rds.aliyuncs.com"
redis_port=6379
redis_password="Kuangbiao123456"
r=redis.StrictRedis(host=redis_host,port=redis_port,password=redis_password,decode_responses=True)
print("Connected to redis via "+redis_host)

t = time.localtime()
current_time = time.strftime("%Y%m%d", t)
print(current_time)

for code in codes:
    code=code.replace("\n","")
    pattern=code+'_'+current_time+'*'
    print(pattern)
    keys=r.keys(pattern)
    keys=sorted(keys,reverse=True)
    print(keys)
    for key in keys:
        print(key+":"+r.get(key))


