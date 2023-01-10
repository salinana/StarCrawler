import os

file=open('man.cn.txt','r')
lines=file.readlines()
newfile=open('cn.man.txt','w')
count = 0
# Strips the newline character
for line in lines:
    count += 1
    print(count)
    words=str(line).split('|')
    print(words[0])
    print(words[1])
    print(words[2])
    newline="cnm"+str(count)+"|"+line
    newfile.write(newline)