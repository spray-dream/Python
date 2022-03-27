# -*- coding = utf-8 -*-
# @Time : 2021/4/24 19:53
# @Author : spray_dream
# @File : 循环代码优化测试.py
# @Software: PyCharm

import time

start1 = time.time()
for i in range(1000):
    result = []
    for m in range(10000):
        result.append(i*1000+m*100)

end1 = time.time()
print("耗时:{0}".format((end1-start1)))


start2 = time.time()
for i in range(1000):
    result = []
    c = i*1000    # 避免了i*1000执行10000次,节省程序运行时间
    for m in range(10000):
        result.append(c+m*100)

end2 = time.time()
print("耗时:{0}".format((end2-start2)))

# 其他优化手段,连接多个字符串,尽量使用join()
# 列表对元素进行插入和删除,尽量在列表尾部操作
