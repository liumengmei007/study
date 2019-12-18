import pymysql
import re
db = pymysql.connect(host='localhost',port=3306,
                     user='root',password='123456',
                     database='dict',charset='utf8')
cur = db.cursor()
f=open('/home/tarena/桌面/读/dict.txt')
args_list=[]
for line in f:
    result=re.findall(r"(\S+)\s+(.*)",line)
    args_list.extend(result)
f.close()
x="insert into words (word,mean) values (%s,%s);"
try:
    cur.executemany(x,args_list)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()

# select * from words where id<10;