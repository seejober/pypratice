#! /usr/bin/env python3
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

dblist = myclient.list_database_names()
# dblist = myclient.database_names()
if "runoobdb" in dblist:
    print("数据库已存在！")



mydb = myclient['runoobdb']
collist = mydb.list_collection_names()
# collist = mydb.collection_names()
if "sites" in collist:  # 判断 sites 集合是否存在
    print("集合已存在！")

mydb = myclient["runoobdb"]
mycol = mydb["sites"]

mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

x = mycol.insert_one(mydict)
print(x)
print(x)







