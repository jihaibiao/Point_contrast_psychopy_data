# -*- coding = utf-8 -*-
# @Time : 2022/8/25 21:13
# @Author : 计海彪
# @File : Number.py
# @Software : PyCharm
import os,csv,random,math,numpy


if not os.path.exists('number_file'):
    os.mkdir('number_file')
data_file = open('number_file/'+'D10_W0.8_point_contrast_psychopy'+'.csv','w',encoding='UTF-8',newline='')
writer = csv.writer(data_file)
writer.writerow(["Pos_Current","WIDTH","distance","ID"])

w = 0.8  #圆的直径（width）
base = 100 #倍数
d = 10 #距离为10base
ID = math.log(2 * d/w, 2)

#生成点的范围
x_min = w/2
x_max = 1920/base -w +x_min
y_min = w/2
y_max = 1080/base -w +y_min

i = 1
x_pre = 2
y_pre = 11
while i <= 31:
    x = round(random.uniform(x_pre-d,x_pre+d),3)
    if x_min < x < x_max:
        y_p = round(y_pre + math.sqrt( numpy.square(d)-numpy.square(x-x_pre)),3)
        y_n = round(y_pre - math.sqrt(numpy.square(d) -numpy.square(x - x_pre)),3)
        y = random.choice([y_n,y_p])#一正一负，，随机挑
        if y_min < y < y_max:
            writer.writerow([[round(x * base - 960, 0), round( 540 - y * base, 0)], w * base, d *base ,round (ID,3)])  # 转换成psychopy里面的坐标
            x_pre = x
            y_pre = y
            i += 1