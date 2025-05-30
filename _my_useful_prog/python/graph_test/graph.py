import numpy as np
from graph_template import GraphWindow, Graph
import os


# プログラムのあるディレクトリ
scriptDir = os.path.dirname(os.path.abspath(__file__))

# 2行1列で全体サイズ指定
graphWindow = GraphWindow(figsize=(7, 7))

# x軸データ
x = np.linspace(-2, 2, 500)

f = np.cos(x) - x**2


# 1枚目: 縦比率のみ指定（1列なのでheight_ratioのみ有効）
g1 = Graph(height_ratio=1)

g1.add_function(x, f, label="")

g1.set_labels(xlabel="x", ylabel="y", title="")
# g1.set_range(xlim=(-1, 3), ylim=(-5, 1))




graphWindow.add_graph(g1)
g1.save(os.path.join(scriptDir, "g1.png"))

graphWindow.save_all(os.path.join(scriptDir, "g.png"))
graphWindow.show()
