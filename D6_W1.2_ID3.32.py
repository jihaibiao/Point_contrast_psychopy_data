# -*- coding = utf-8 -*-
# @Time : 2022/8/25 21:13
# @Author : 计海彪
# @File : Number.py
# @Software : PyCharm
import os,csv,random,math,numpy


if not os.path.exists('number_file'):
    os.mkdir('number_file')
data_file = open('number_file/'+'D6_W1.2_point_contrast_psychopy'+'.csv','w',encoding='UTF-8',newline='')
writer = csv.writer(data_file)
writer.writerow(["Pos_Current","WIDTH","distance","ID"])

screen_x = 1024
screen_y = 768
w = 1.2  #圆的直径（width）
base = 100 #倍数
d = 6 #距离为10base
ID = math.log(2 * d/w, 2)


#生成点的范围
x_min = w/2
x_max = screen_x/base -w +x_min
y_min = w/2
y_max = screen_y/base -w +y_min

i = 1
x_pre = screen_x/base
y_pre = 0
writer.writerow([[round(x_pre * base - screen_x/2, 0), round( y_pre * base - screen_y/2, 0)], w * base, d *base ,round (ID,3)])
while i <= 32:
    x = round(random.uniform(x_pre-d,x_pre+d),3)
    if x_min < x < x_max:
        y_p = round(y_pre + math.sqrt( numpy.square(d)-numpy.square(x- x_pre)),3)
        y_n = round(y_pre - math.sqrt(numpy.square(d) -numpy.square(x - x_pre)),3)
        y = random.choice([y_n,y_p])#一正一负，，随机挑
        if y_min < y < y_max:
            writer.writerow([[round(x * base - screen_x/2, 0), round( y * base - screen_y/2, 0)], w * base, d *base ,round (ID,3)])  # 转换成psychopy里面的坐标
            x_pre = x
            y_pre = y
            i += 1
