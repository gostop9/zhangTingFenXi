# -*- coding: utf-8 -*-
import os
import re

continueLimit_file = 'D:/share/continueLimit.txt'
if os.path.exists(continueLimit_file): # 如果文件存在
    #删除文件，可使用以下两种方法。
    os.remove(continueLimit_file) # 则删除
    
ztProportionFileName = 'D:/share/ztProportion.txt'
if os.path.exists(ztProportionFileName): # 如果文件存在
    #删除文件，可使用以下两种方法。
    os.remove(ztProportionFileName) # 则删除
    
buyShare_file = 'D:/share/buyShare.txt'
if os.path.exists(buyShare_file): # 如果文件存在
    os.remove(buyShare_file) # 则删除
    
firstLiuRu_file = 'D:/share/firstLiuRu.txt'
if os.path.exists(firstLiuRu_file): # 如果文件存在
    os.remove(firstLiuRu_file) # 则删除
    
cfg_flie = "D:/share/config.txt"

f1 = open(cfg_flie, "r")
lines = f1.readlines()
num = len(lines)
f1.close()

lines_org = lines.copy()

f_zt = open("D:/share/zhangTingConfig.txt", "r")
ztLines = f_zt.readlines()
ztNum = len(ztLines)
lines[3] = 'result_zt.txt\n'
for i in range(ztNum-1):
    if (ztLines[i] != '\n'):
        # modify config.txt file
        f2 = open("D:/share/config.txt", "w")
        
        lines[0] = ztLines[i+1][0:9] + '\n'
        lines[1] = '1\n'
        '''
        lines[0] = ztLines[i][0:9] + '\n'
        listTemp = ztLines[i].split('_')
        lines[1] = listTemp[1]
        '''
        print (str(lines[0]) + '\n')
        lines[11] = '2.05\n'
        lines[12] = ztLines[i]
        if (i > 1):
            lines[13] = ztLines[i-1]
            lines[14] = ztLines[i-2]
        f2.writelines(lines[0:15])
        f2.write('\n')
        f2.close()

        main = u'D:/share/shareAnalyze/shareAnalyze/x64/Release/shareAnalyze.exe'
        r_v = os.system(main)
        print(r_v)
        
        '''
        #统计连续涨停
        ztFileName0 = ztLines[i  ][0:8] + '.txt'
        ztFileName1 = ztLines[i+1][0:8] + '.txt'
        f_zt0 = open(ztFileName0, "r")
        f_zt1 = open(ztFileName1, "r")
        ztLines0 = f_zt0.readlines()
        ztLines1 = f_zt1.readlines()
        '''
f_zt.close()

f2 = open(cfg_flie, "w")
f2.writelines(lines_org)
f2.close()

f_ztProportion = open(ztProportionFileName, "r")
ztLines = f_ztProportion.readlines()
f_ztProportion.close()
ztNum = len(ztLines)

nums = re.findall(r"\d+\.?\d*", ztLines[i])
list = [0.0] * len(nums)
for i in range(ztNum):
    nums = re.findall(r"\d+\.?\d*", ztLines[i])
    for j in range(len(nums)):
        list[j] += float(nums[j])

f_ztProportion = open(ztProportionFileName, 'a+')
f_ztProportion.write('\n')
secNum = int(len(nums)/2)
for i in range(secNum):
    text = '{:f}, {:f}, '.format(list[2*i], list[2*i+1])
    f_ztProportion.write(str(text))
f_ztProportion.write('\n')
for i in range(secNum):
    text = '{:f}, '.format(list[2*i+1]/list[2*i])
    f_ztProportion.write(str(text))
f_ztProportion.write('\n')
f_ztProportion.close()
    