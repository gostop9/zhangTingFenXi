# -*- coding: utf-8 -*-
import os

f1 = open("D:/share/config.txt", "r")
lines = f1.readlines()
num = len(lines)
f1.close()

lines_org = lines.copy()

f_zt = open("D:/share/zhangTingConfig.txt", "r")
ztLines = f_zt.readlines()
ztNum = len(ztLines)
ztLines.append('end')
startLine = 0
lines[3] = 'result_zt.txt\n'
for i in range(ztNum):
    if (ztLines[i] == '\n'):
        endLine = i
        if(endLine - startLine < 2):
            break
        # modify config.txt file
        f2 = open("D:/share/config.txt", "w")
        lines[0] = ztLines[startLine][0:9] + '\n'
        lines[1] = ztLines[startLine][9:]
        lines[11] = '2.05\n'
        lines[12] = ztLines[startLine + 1]
        lines[13:] = ztLines[startLine + 2 : endLine]
        f2.writelines(lines)
        #f2.writeline('\n')
        f2.close()
        startLine = endLine + 1

        main = u'D:/share/shareAnalyze/shareAnalyze/x64/Release/shareAnalyze.exe'
        r_v = os.system(main)
        print(r_v)
f_zt.close()

f2 = open("D:/share/config.txt", "w")
f2.writelines(lines_org)
f2.close()

