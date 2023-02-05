from operator import itemgetter

database_cnm=open("database/cnm.records.txt","r")
database_cnw=open("database/cnw.records.txt","r")
database_hkm=open("database/hkm.records.txt","r")
database_hkw=open("database/hkw.records.txt","r")
database_twm=open("database/twm.records.txt","r")
database_tww=open("database/tww.records.txt","r")

records=[]
list=database_cnm.readlines()+database_cnw.readlines()+database_hkm.readlines()+database_hkw.readlines()+database_twm.readlines()+database_tww.readlines();
for star in list:
    temp=star.split("|")
    temp[1]=int(temp[1])
    records.append(tuple(temp))
srecords=sorted(records,key=itemgetter(1),reverse=True)

for record in srecords:
    print(record)


database=open("database/database.js","w")

database.write("const database=[")

for tuple in srecords:
    record = tuple[0] + "|" + str(tuple[1]) + "|" + tuple[2] + "|" + tuple[3] + "|" + tuple[4] + "|" + tuple[5] + "|" + \
             tuple[6] + "|" + tuple[7] + "|" + tuple[8] + "|" + tuple[9] + "|" + tuple[10] + "|" + tuple[11].replace(
        "\n", "")
    database.write("\n"+"'"+record+"'"+",")
database.write("]")