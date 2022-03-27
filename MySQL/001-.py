# -*- coding = utf-8 -*-
# @Time : 2022/2/27 20:35
# @Author : spray_dream
# @File : 001-.py
# @Software: PyCharm

import pymysql

# 1.链接MySQL数据库
db = pymysql.connect(host='localhost',
                     user='root',
                     password='340915',
                     db='test001',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

# 2.创建游标对象
cursor = db.cursor()

# 3.准备sql语句
sql = 'select version()'

# 4.执行sql语句
cursor.execute(sql)

# 5.提取结果
data = cursor.fetchall()

# 6.关闭数据库连接
db.close()

print(data)
