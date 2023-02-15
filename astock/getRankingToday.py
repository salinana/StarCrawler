import redis
import time
import oss2

redis_host="kuangbiao.redis.rds.aliyuncs.com"
redis_port=6379
redis_password="Kuangbiao123456"
r=redis.StrictRedis(host=redis_host,port=redis_port,password=redis_password,decode_responses=True)
print("Connected to redis via "+redis_host)

t = time.localtime()
current_time = time.strftime("%Y%m%d_%H:%M:%S", t)
print(current_time)

t = time.localtime()
today_date= time.strftime("%Y%m%d", t)
current_time = time.strftime("%Y%m%d_%H", t)
print(current_time)
ranking_dict={}
keys=r.keys("*_"+current_time+"*")
keys=sorted(keys)
for key in keys:
    print(key)
    code=key.split("_")[0]
    ranking_dict[code]=[]
print(ranking_dict)

for key in keys:
    code = key.split("_")[0]
    value=r.get(key)
    if value!="" and value!="-":
        ranking_dict[code].append(value)

print(ranking_dict)
auth = oss2.Auth('LTAI5tEqJynXSSPoVK9QkcWe', 'Db4tR6QqUlNdnmYjPLQoSnp2ne9F2F')
bucket = oss2.Bucket(auth, 'oss-cn-shenzhen.aliyuncs.com', 'kuangbiao')
bucket.put_object(today_date+"/"+current_time+".txt",str(ranking_dict))

t = time.localtime()
current_time = time.strftime("%Y%m%d_%H:%M:%S", t)
print(current_time)