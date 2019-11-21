# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:25:41 2019

@author: Yugar
"""

def init_dict(chars, dic):
    for char in chars:
        if str(len(dic.keys())) not in dic.keys():
            dic[str(len(dic.keys()))] = char

codestream = '01243'
charstream = ''

# 初始化字典
#读取
f = open('temp.txt','r')
a = f.read()
String = eval(a)
f.close()
String = dict(zip(String.values(), String.keys()))
print(String)

index = 0

cW = codestream[index]
charstream += String[cW]
P = String[cW]
pW = cW

index += 1


while index < len(codestream):
    cW = codestream[index]
    # 在String中
    if cW in String.keys():
        charstream += String[cW]
        P = String[pW]
        C = String[cW] # 取 String.cW 的首字母，进行字典扩展
        String[str(len(String.keys()))] = P + C
    else:
        P = String[pW]
        C = P[0]
        charstream += (P + C) # 取 String.pW 的首字母，进行字典扩展
        String[str(len(String.keys()))] = P + C
    pW = cW
    index += 1

print(charstream)