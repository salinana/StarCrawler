import os
import re
from operator import itemgetter

from city import getArea


def getChinese(context):
    #context = context.decode("utf-8") # convert context from str to unicode
    filtrate = re.compile(u'[^\u4E00-\u9FA5]') # non-Chinese unicode range
    context = filtrate.sub(r'', context) # remove all non-Chinese characters
    #context = context.encode("utf-8") # convert unicode back to str
    return context
def getDigit(context):
    #context = context.decode("utf-8") # convert context from str to unicode
    filtrate = re.compile(u'[^\d+]') # non-Chinese unicode range
    context = filtrate.sub(r'', context) # remove all non-Chinese characters
    #context = context.encode("utf-8") # convert unicode back to str
    return context
database=open("database/hkw.records.txt","w")
records=[]
file=open('urls/hk.woman.txt', 'r')
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
    imgUrl=words[3]
    detailUrl="profiles/hkw/"+index+name+"/"+index+name+".txt"
    if not os.path.exists(detailUrl):
        continue
    pfile = open(detailUrl, 'r')
    dLines=pfile.readlines()

    for dline in dLines:
        print(dline)
        if "中文名" in dline.split(":")[0].replace("\n",""):
            name = dline.split(":")[1].replace("\n", "").strip()
            name = name.split("[")[0].strip()
        if "浏览次数" in dline.split(":")[0].replace("\n",""):
            visit=dline.split(":")[1].replace("\n","").strip()
        if "出生日期" in dline.split(":")[0].replace("\n",""):
            year=re.search(":(.+?)年",dline)
            if year:
                year=year.group(1)
            else:
                year="*"
            month=re.search("年(.+?)月",dline)
            if month:
                month=month.group(1)
            else:
                month = re.search(":(.+?)月", dline)
                if month:
                    month=month.group(1)
                else:
                    month="*"
            day=re.search("月(.+?)日",dline)
            if day:
                day=day.group(1)
            else:
                day="*"

            year=getDigit(year)
            month=getDigit(month)
            day=getDigit(day)
        if "职业" in dline.split(":")[0].replace("\n",""):
            job=dline.split(":")[1].replace("\n","")
            job=job.split("、")[0]
            job=getChinese(job)

        if "运动项目" in dline.split(":")[0].replace("\n",""):
            job="运动员"

        if "国籍" in dline.split(":")[0].replace("\n",""):
            country=dline.split(":")[1].replace("\n","")
            country=getChinese(country)
        if "出生地" in dline.split(":")[0].replace("\n",""):
            # province=dline.split(":")[1].replace("\n","")
            # province=re.search(":(.+?)省",dline)
            # if province:
            #     province=province.group(1)
            # else:
            #     province="*"
            # city = dline.split(":")[1].replace("\n", "")
            # city = re.search("省(.+?)市", dline)
            # if city:
            #     city = city.group(1)
            # else:
            #     city = re.search(":(.+?)市", dline)
            #     if city:
            #         city=city.group(1)
            #     else:
            #         city=dline.split(":")[1].replace("\n", "")
            # if "香港" in dline:
            #     province="香港"
            #     city="香港"
            # if "澳门" in dline:
            #     province = "澳门"
            #     city = "澳门"
            # if "台湾" in dline:
            #     province="台湾"
            #     city="台湾"
            province,city=getArea(dline.split(":")[1].replace("\n", ""))
    record = index + "|"+visit +"|"+ name + "|" + "M"+"|"+year+"|"+month+"|"+day+"|"+job+"|"+country+"|"+province+"|"+city+"|"+imgUrl
    print(record)
    if visit and int(visit)>=1000000:
        tuple = (index, int(visit), name, "F", year, month, day, job, country, province, city, imgUrl)
        records.append(tuple)

    year = ""
    month = ""
    day = ""
    country = ""
    province = ""
    city = ""
    job = ""

srecords=sorted(records,key=itemgetter(1),reverse=True)

# database.write("const database=[")
previous=""

for tuple in srecords:
    record=tuple[0]+"|"+str(tuple[1])+"|"+tuple[2]+"|"+tuple[3]+"|"+tuple[4]+"|"+tuple[5]+"|"+tuple[6]+"|"+tuple[7]+"|"+tuple[8]+"|"+tuple[9]+"|"+tuple[10]+"|"+tuple[11].replace("\n","")
    if previous!=tuple[2]+tuple[3]+tuple[4]:
        previous = tuple[2]+tuple[3]+tuple[4]
        # database.write("\n"+"'"+record+"'"+",")
        database.write(record + "\n")
        print(record)
# database.write("]")