import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-4, 4, 0.1)  # xを-4から4まで0.1刻みで用意
y1 = x**2+2*x+1
y2 = x*2+10
plt.title("4kai_kadai")  # グラフのタイトル
plt.xlabel("x")  # x軸（横軸）のラベル
plt.ylabel("y")  # y軸（縦軸）のラベル
plt.plot(x, y1, label="x**2 + x*2 + 1")  # labelに凡例に表示する文字を指定
plt.plot(x, y2, label="x*2 + 10")
plt.legend()  # 凡例を表示
plt.show()  # プロットしたグラフを画面に表示

