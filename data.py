# -*- coding = utf-8 -*-
# @Time : 2022/9/15 21:08
# @Author : 计海彪
# @File : data.py
# @Software : PyCharm
import os,csv,random,math


if not os.path.exists('number_file'):
    os.mkdir('number_file')
data_file = open('number_file/'+'number_ap_psychopy'+'.csv','w',encoding='UTF-8',newline='')
writer = csv.writer(data_file)
writer.writerow(["Pos_Current","WIDTH","distance","ID"])
X=[2,8.6,15.2]
Y=[2,6.5,11]
i = 1
while i <= 136:
    x = random.choice(X)
    y = random.choice(Y)
    w = random.randint(1,3)
    if i > 1:
        while x == x_pre and y == y_pre:
            x = random.choice(X)
            y = random.choice(Y)
        d = math.sqrt((x - x_pre)**2 + (y - y_pre )**2 )
        ID = math.log(2 * d/w, 2)
    else:
        d = 0
        ID = 0

    x_pre = x
    y_pre = y
    base = 80

    writer.writerow([[round(x * base - (17.2 * base ) / 2, 0), round(y * base - (13 * base) / 2, 0)], w * base, round(d * base,0),round (ID,3)])  # 转换成psychopy里面的坐标
    i += 1
