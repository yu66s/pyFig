# coding:utf-8


# plt.rcdefaults()


import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']

clname = (u'本地VB准备', u'子本地VB准备/Wi Fi', u'子本地VB准备/3G', u'VB准备/Wi Fi', u'VB准备/3G', u'外部/Wi Fi', u'外部/3G')
y_label = [7, 6, 5, 4, 3, 2, 1]
x_label = [1, 2, 3, 4, 5, 6, 7]
y_pos = [7, 6, 5, 4, 3, 2, 1]
width = np.array([0.25, 0.5, 0.8, 0.55, 0.95, 1.68, 1.82])
plt.barh(bottom=y_pos, width=width, align='center', alpha=0.4)
for a, b, c in zip(y_label, width, clname):
    plt.text(y=a, x=b+0.1, s=c)
plt.ylabel(u'实例')
plt.xlabel(u'点击播放延迟（秒）')
plt.yticks(y_pos, y_label)
plt.xlim(0,3)
plt.show()
plt.savefig("b3.eps",format="png")
