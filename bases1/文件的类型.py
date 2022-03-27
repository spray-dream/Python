# 文件与python程序必须放在同一目录下,这样才是同级目录
a = open('1.txt', 'rt')    # r代表read,读取;t代表txt文本文档类型,文件经过编码形成字符串
print(a.readline())     # readline是读取文本内容
a.close()

a = open('1.txt', 'rb')    # r代表read,读取;b表示以二进制方式打开,文件被解析为字节流
print(a.readline())
a.close()
