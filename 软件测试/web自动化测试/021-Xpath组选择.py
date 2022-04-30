# -*- coding = utf-8 -*-
# @Time : 2022/4/30 23:21
# @Author : spray_dream
# @File : 021-Xpath组选择.py
# @Software: PyCharm
pass
"""
类似于CSS选择中的逗号,Xpath中也有组选择,使用|
option , h4
    //option | //h4
选择所有class属性为single_choice和multi_choice的标签,等同于.single_choice , .multi_choice
    //*[@class='single_choice'] | //*[@class='multi_choice']
"""

"""
Xpath独有的,选择父标签,用/..表示
选择id为china的标签的父标签
    //*[@id='china']/..
父标签的父标签
    /../..
"""

"""
兄弟节标签选择用following-sibling::
.single_choice ~ *选择class属性为single_choice的标签的所有后续兄弟标签(不包括任意父标签下class属性为single_choice的第一个标签)
    //*[@class='single_choice']/following-sibling::*
.single_choice ~ div选择class属性为single_choice的标签的所有后续是div的兄弟标签
    //*[@class='single_choice']/following-sibling::div
可以选择前面的兄弟标签将follow改成preceding-sibling::(CSS不能直接选择前面的兄弟标签)
"""

"""
使用Xpath需要注意的一点是要在某个标签内部使用xpath选择标签,需要在xpath表达式最前面加个点,这样找到的//p才不会是HTML代码全部范围的
例如:
# 先寻找id是china的标签
china = wd.find_element(By.ID, 'china')
# 再选择该元素内部的p标签
elements = china.find_elements(By.XPATH, './/p')
"""
