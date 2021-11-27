# -*- coding: utf-8 -*-
from case.readxls import Readxls
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Microsoft JhengHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

def draw_pie(labels,quants):


    plt.figure(1, figsize=(6,6))

    colors  = ["blue","red","coral","green","yellow","orange"]  #设置颜色（循环显示）
    # 0.1表示将B那一块凸显出来
    explode = (0.1, 0.1, 0.1, 0.1,0.1,0.1)
    x = quants
    # 绘制饼图,autopct='%.0f%%' 显示百分比
    # textprops = {'fontsize':30, 'color':'k'} 大小为30，颜色为黑色
    # explode=explode 将B那一块凸显出来




    plt.pie(x,explode = explode,labels = labels, colors=colors, autopct='%1.1f%%',pctdistance=0.5, shadow=True)
    plt.title('2009-2004年度改判发回案件分布情况', bbox={'facecolor':'0.8', 'pad':5})
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')

    plt.legend(loc="lower right")

    plt.savefig("2009-2004年度改判发回案件分布情况.png")
    plt.show()
    # 输出图片
    plt.close()



if __name__ == '__main__':
    datas = []
    datas = Readxls().read_data()
    print(datas[0])
    print(datas[1])
    print(datas[2])
    labels = datas[1]
    quants = datas[2]
    draw_pie(labels, quants)
    #在这里运行

