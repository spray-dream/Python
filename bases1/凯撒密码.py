ptxt=input('请输入明文文本')
for p in ptxt:
    if 'a'<=p<='z':
        print(chr(ord('a')+(ord(p)-ord('a')+3)%26),end='')
    elif'A'<=p<='Z':
        print(chr(ord('A')+(ord(p)-ord('a')+3)%26),end='')
    else:
        print(p,end='')