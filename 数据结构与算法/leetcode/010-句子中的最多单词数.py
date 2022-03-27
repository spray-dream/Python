# -*- coding = utf-8 -*-
# @Time : 2022/2/22 23:13
# @Author : spray_dream
# @File : 010-句子中的最多单词数.py
# @Software: PyCharm

sentences = ['1 2 3', '4 5', '6']
n = len(sentences)
ans = []
for i in range(n):
    sentences[i] = sentences[i].split(' ')
    ans.append(len(sentences[i]))

ans.sort()
print(ans[-1])
print(sentences)
