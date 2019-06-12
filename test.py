import pandas as pd
import datetime
import pymysql as py


# enter_time = datetime.datetime.now().strftime("%Y-%m-%d")
# tt = datetime.datetime.
# list1 = []
# list2 = []
# df = pd.read_excel('newcsvfile1.xlsx')
# dates = pd.to_datetime(df['PublishDate'], format='%Y%m%d')
# ee = dates.apply(lambda x: x.strftime('%Y-%m-%d'))
#
# for i in df['Reso']:
#     list1.append(i)
# for j in ee:
#     list2.append(j)
# for z in zip(list1, list2):
#     newz = z[0] + z[1]
#     sql = "insert into perus(reso_and_pub,enter_time) VALUES ('%s','%s')" % (newz, enter_time)
#     cursors.execute(sql)
#     db.commit()
# cursors.close()
# db.close()
# df=df.sort_values(by="PublishDate", ascending=False)
# df.to_excel('ws.xlsx', index=False)
# o = '23/07/2018'
# date = datetime.datetime.strptime(o, '%d/%m/%Y')
# print(date.strptime())
# startDate = "2018-10-01"
# endDate = "2018/10/31"
#
##字符转化为日期
# startTime = datetime.datetime.strptime(startDate, '%Y-%m-%d')
# endTime = datetime.datetime.strptime(endDate, '%Y/%m/%d')
# print((endTime))
# now = datetime.datetime.now()
# print(now)

###日期转化为字符串
# print("--1---:" + datetime.datetime.strftime(startTime, "%Y-%m-%d"))
# print("--2---:" + datetime.datetime.strftime(endTime, "%Y/%m/%d"))
# writer=pd.ExcelWriter("test.xlsx")
# df=pd.DataFrame(df)   #如果df是Series对象，则需要转换为DataFrame对象
#
# #添加一列数据df["time"]
# df["time"]=df.index.strftime("%Y/%m/%d %H:%M:%S")
# #选择性写入
# df.t
# df = pd.read_excel('2018_08_13.xlsx')
# df['PublishDate'] = pd.to_datetime(df.PublishDate)
# df['PublishDate'] = df['PublishDate'].dt.strftime('%Y-%m-%d')
# pub = str(df['PublishDate'])
# date = datetime.datetime.strptime(pub, '%Y-%m-%d')
# print(pub)
# df.to_excel('wang.xlsx', index=False)
#
# df.head()
# writer.save()
