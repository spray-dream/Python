def newFile():
    try:
        f = open("gushi.txt", "w")
        while True:    # 逐行输入内容
            line = input("输入一行,空格退出:")
            f.write(line)
            f.write("\n")
            if line == " ":
                break
    except Exception as e:
        print(e)
        print("文件新建发生错误")
    else:    # try中没有异常时执行
        print("gushi.txt新建成功")
    # 此处应有删除文件末尾空格和换行的代码(待解决)
    f.close()


def copyFile():
    try:
        newFile()
        with open("gushi.txt", "r") as f:
            a = f.readlines()
        with open("../../IT基础/copy.txt", "w") as F:
            for i in a:    # 逐行复制
                F.write(i)
    except Exception as e:
        print(e)
        print("复制发生错误")
    else:
        print("复制完毕")
    finally:
        print('无论try是否异常,都会执行.一般在这里执行清理,关闭等操作')


copyFile()
F = open("../../IT基础/copy.txt", "r")
data = F.read()
print("copy.txt文件中的内容是:", data)    #  12    (为什么12前面有空格)
                                        # 23
                                        #
print(data)

import os
os.remove("gushi.txt")
