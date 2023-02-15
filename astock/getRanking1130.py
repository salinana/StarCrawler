import redis
from datetime import datetime,time as timeA
import time
import sys

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

while 1:

    if not is_time_between(timeA(11,00), timeA(12,10)):
        print("Continue")
        continue

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
    current_time = time.strftime("%Y%m%d_11", t)
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

    for kk, vv in ranking_dict.items():
        print(kk, vv)
        delta=0
        if len(vv)>=2:
            delta=int(vv[0])-int(vv[-1])
        if delta>1000:
            print("Best:"+kk)
            Sample.main(""+kk, sys.argv[1:])

    t = time.localtime()
    current_time = time.strftime("%Y%m%d_%H:%M:%S", t)
    print(current_time)