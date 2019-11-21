# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:20:50 2019

@author: Yugar
"""

def init_dict(chars, dic):
    for char in chars:
        if char not in dic.keys():
            dic[char] = str(len(dic.keys()))

charstream = 'ababababa'
codestream = ''

# 初始化字典

dic = dict()
init_dict(charstream, dic)

# 保存初始化字典
f = open('temp.txt','w')
f.write(str(dic))
f.close()


index = 0

P = ''

while index < len(charstream):
    C = charstream[index]
    if (P + C) in dic.keys():
        P += C
    else:
        # 输出到码流
        codestream += dic[P]
        # 新增字典值
        dic[P + C] = str(len(dic.keys()))
        # 重新开始计数
        P = C
    index += 1 

codestream += dic[P]

print("original code:", charstream)
print("compressed code:", codestream)
