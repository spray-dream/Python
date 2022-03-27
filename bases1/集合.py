# 如果1是集合s里的元素,返回True
s = {1, 2, 3}
print(1 in s)

# 空集合时
s = set({})
print(s, type(s))
# 或者
s = set()
print(s, type(s))  # 以上两项都能把输入的东西转换成集合,并自动去重
# 注,此时是字典类型
s = {}
print(s, type(s))

# 遍历之后
s = set('12345')
print(s, type(s))
for i in s:
    print(i, type(i))
