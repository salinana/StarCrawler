import redis
from datetime import datetime,time as timeA
import time
import sys
import threading

from typing import List

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Dysmsapi20170525Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id="LTAI5tEqJynXSSPoVK9QkcWe",
            # 必填，您的 AccessKey Secret,
            access_key_secret="Db4tR6QqUlNdnmYjPLQoSnp2ne9F2F"
        )
        # 访问的域名
        config.endpoint = f'dysmsapi.aliyuncs.com'
        return Dysmsapi20170525Client(config)

    @staticmethod
    def main(
        code,
        args: List[str]
    ) -> None:
        # 工程代码泄露可能会导致AccessKey泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            sign_name='阿里云短信测试',
            template_code='SMS_154950909',
            phone_numbers='13539563922',
            template_param='{"code":"'+code+'"}'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            client.send_sms_with_options(send_sms_request, runtime)
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 工程代码泄露可能会导致AccessKey泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            sign_name='阿里云短信测试',
            template_code='SMS_154950909',
            phone_numbers='13539563922',
            template_param='{"code":"1234"}'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.send_sms_with_options_async(send_sms_request, runtime)
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)

def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.now().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time


the_file = open('stocklistv.txt', 'r')
lines = the_file.readlines()
the_file.close()

redis_host = "kuangbiao.redis.rds.aliyuncs.com"
redis_port = 6379
redis_password = "Kuangbiao123456"
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
print("Connected to redis via " + redis_host)


def getRank(threadname,start_num,end_num):

    while 1:

        if not is_time_between(timeA(22,00), timeA(12,1)):
            print("Continue")
            continue

        print("Start")

        t = time.localtime()
        today_date= time.strftime("%Y%m%d", t)

        for line in lines[start_num:end_num]:
            code=line.replace("\n","")

            pattern=code+"_"+today_date+"_11:0*"
            keys=r.keys(pattern)
            if len(keys)<1:
                continue
            startValue=r.get(keys[0])
            pattern=code+"_"+today_date+"_11:5*"
            keys=r.keys(pattern)
            if len(keys)<1:
                continue
            endValue=r.get(keys[0])

            if startValue=="" or startValue=="-" or endValue=="" or endValue=="-":
                continue
            delta=int(startValue)-int(endValue)

            print(threadname+":"+code+":"+str(delta))

            if delta>2000:
                print("Best:"+code+"-->"+str(delta))
                # Sample.main(""+code, sys.argv[1:])
                # time.sleep(61)

        print("End")


thread1= threading.Thread(target=getRank,args=["thread1[0-500]",0,500])
thread1.start()

thread2= threading.Thread(target=getRank,args=["thread2[500-1000]",500,1000])
thread2.start()

thread3= threading.Thread(target=getRank,args=["thread3[1000-1500]",1000,1500])
thread3.start()

thread4= threading.Thread(target=getRank,args=["thread4[1500-2000]",1500,2000])
thread4.start()

thread5= threading.Thread(target=getRank,args=["thread5[2000-2500]",2000,2500])
thread5.start()

thread6= threading.Thread(target=getRank,args=["thread6[2500-3000]",2500,3000])
thread6.start()

thread7= threading.Thread(target=getRank,args=["thread7[3000-3500]",3000,3500])
thread7.start()

thread8= threading.Thread(target=getRank,args=["thread8[3500-4000]",3500,4000])
thread8.start()

thread9= threading.Thread(target=getRank,args=["thread9[4000-4500]",4000,4500])
thread9.start()

thread10= threading.Thread(target=getRank,args=["thread10[4500-5500]",4500,5500])
thread10.start()