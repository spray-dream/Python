# -*- coding = utf-8 -*-
# @Time : 2021/3/27 12:31
# @Author : spray_dream
# @File : 格式化.py
# @Software: PyCharm

# 标识符
import keyword
print(keyword.kwlist)

# 格式化输出
age = 20
name = 'abc'
print('我的名字是:%s,我的年纪是%d岁,我的国籍是%s' % (name, age, '中国'))
# %是占位符.d是decimal,十进制.s是字符串格式,格式符号有很多

print('www', 'baidu', 'com', sep='.')    # sep是分隔,不加sep时默认空格
print(1234, end='\n')
print(12)    # end='\n'换行,与不加end是一样的效果
print('1234\n12')    # \n后的内容换行显示

print(id(3))    # 2232231750000