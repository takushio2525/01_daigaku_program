import numpy as np
from graph_template_class import GraphWindow, Graph
import os

# data_list = [[-2, 0], [-1, 2], [0, 4], [1, 5], [2, 8]]  # 2次元配列のリストに変更
data_list = [[1, 8], [2, 11], [3, 10], [4, 12], [5, 13]]  # 2次元配列のリストに変更

x_values = [x for x, _ in data_list]
x_mean = sum(x_values) / len(x_values)

print(f"左の値の平均: {x_mean}")

y_values = [y for _, y in data_list]
y_mean = sum(y_values) / len(y_values)

print(f"みぎの値の平均: {y_mean}")

sig1 = 0
sig2 = 0

for i in range(len(x_values)):
    sig1 += (x_values[i] - x_mean) * (y_values[i] - y_mean)
    sig2 += (x_values[i] - x_mean) ** 2

b1 = sig1/sig2

print("b1=" + str(b1))

b0 = y_mean-b1*x_mean
print("b0=" + str(b0))

risou = []  # 空のリストを初期化

for i in range(len(data_list)):
    x = data_list[i][0]  # x座標を取得
    y_pred = b0 + b1 * x  # 回帰直線のy値を計算
    risou.append((x, y_pred))  # リストに追加

print("risou=" + str(risou))

e4 = data_list[3][1]-risou[3][1]
e5 = data_list[4][1]-risou[4][1]

print("e4=" + str(e4))
print("e5=" + str(e5))

sst = 0
ssr = 0
sse = 0
for i in range(len(data_list)):
    sst += (data_list[i][1]-y_mean)**2
    ssr += (risou[i][1]-y_mean)**2
    sse += (data_list[i][1]-risou[i][1])**2

r2 = ssr/sst
print("sst=" + str(sst))
print("ssr=" + str(ssr))
print("sse=" + str(sse))
print("r^2=" + str(r2))


y_risou = [y for _, y in risou]
x1 = np.linspace(-10, 10, 500)
f1 = b0+b1*x1
graphWindow = GraphWindow(figsize=(5, 5), layout="vertical")
g1 = Graph()
g1.add_function(x_values, y_values, plot_type="scatter")  # 散布図として描画
g1.add_function(x_values, y_risou)  # 散布図として描画
g1.add_function(x1, f1)  # 散布図として描画

g1.set_labels(xlabel="x", ylabel="y", title="回帰分析")
# g1.set_range(xlim=(0, 7), ylim=(7, 14))

graphWindow.add_graph(g1)  # グラフを追加

graphWindow.show()
