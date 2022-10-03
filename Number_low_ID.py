# -*- coding = utf-8 -*-
# @Time : 2022/8/25 21:13
# @Author : 计海彪
# @File : Number.py
# @Software : PyCharm
import os,csv,random,math,numpy


if not os.path.exists('number_file'):
    os.mkdir('number_file')
data_file = open('number_file/'+'number_low_point_contrast_psychopy'+'.csv','w',encoding='UTF-8',newline='')
writer = csv.writer(data_file)
writer.writerow(["Pos_Current","WIDTH","distance","ID"])
#生成点的范围
x_min = 0.5
x_max = 18.5 #(x_max -x_min + w) *base < 1920
y_min = 0.5
y_max = 10 #(y_max -y_min + w) *base < 1080
w = 1
base = 100
d = 2
ID = math.log(2 * d/w, 2)

i = 1
x_pre = 2
y_pre = 2
while i <= 31:
    x =  round(random.uniform(x_pre-2,x_pre+2),3)
    if x_min < x < x_max:
        y_p = round(y_pre + math.sqrt(4-numpy.square(x-x_pre)),3)
        y_n = round(y_pre - math.sqrt(4 - numpy.square(x - x_pre)),3)
        y = random.choice([y_n,y_p])#一正一负，，随机挑，距离为2base
        if y_min < y < y_max:
            writer.writerow([[round(x * base - (17.2 * base ) / 2, 0), round(y * base - (13 * base) / 2, 0)], w * base, d *base, round (ID,3)])  # 转换成psychopy里面的坐标
            x_pre = x
            y_pre = y
            i += 1
