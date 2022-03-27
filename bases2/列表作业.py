products = [["iphone", 6888], ["MacPro", 14800], ["coffee", 31], ["Book", 60], ["Nike", 699]]
a = []
b = []
n = 0
for i in products:
    print("序号%d的商品是%s,\n价格为%d" % (n, i[0], i[1]), end="\n")
    n += 1
while True:
    goods = eval(input("请输入商品编号(按5退出):"))    
    if goods == 5:
        break
    a.append(products[goods][0])
    b.append(products[goods][1])
price = 0
for i in b:
    price = price + i
print('您购买的商品有:', a)
print('总价为:', price)
