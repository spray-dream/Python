# 查找某字符在文件里出现了多少次
def times(filename, letter):
    count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        data = data.lower()
        print(data)
        for i in data:
            if i == letter:
                count += 1
            else:
                break
    return count


print(times("计数.txt", 'p'))
# 手机上当文件在此程序的上一级目录时才能运行成功
