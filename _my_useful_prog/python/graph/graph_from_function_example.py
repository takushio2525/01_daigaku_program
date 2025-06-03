import numpy as np
from graph_template_class import GraphWindow, Graph
import os
import pandas as pd

# プログラムのあるディレクトリ
scriptDir = os.path.dirname(os.path.abspath(__file__))

data = pd.read_csv(os.path.join(scriptDir, "data.csv"))

# 横並びのレイアウトに変更
# graphWindow = GraphWindow(figsize=(15, 5), layout="horizontal")
# 縦並びのレイアウトに変更
graphWindow = GraphWindow(figsize=(5, 5), layout="vertical")

x1 = np.linspace(-2, 2, 500)
f1 = np.cos(x1)-x1**2

x2 = np.linspace(-2, 2, 500)
f2 = -np.sin(x2) - 2 * x2
f3 = np.cos(x2)-x2**2


# グラフの定義、全体のうちの比率、グリッドの有無
g1 = Graph()
# 関数を追加
g1.add_function(x1, f1)
g1.set_labels(xlabel="x", ylabel="y", title="f1 = cos(x) - x^2")
g1.set_range(xlim=(-2, 2), ylim=(-2, 2))


# グラフの定義（グリッドや基準線の引数も省略）
g2 = Graph()
g2.add_function(x2, f3)
g2.add_function(x2, f2)
g2.set_labels(xlabel="x", ylabel="y", title="fとfd")
g2.set_range(xlim=(-2, 2), ylim=(-5, 5))
g3 = Graph(size_ratio=1)


graphWindow.add_graph(g1)
graphWindow.add_graph(g2)


# graphWindow.save_all(os.path.join(scriptDir, "func_graph.png"))
# graphWindow.save_graph(g1, os.path.join(scriptDir, "func_g1.png"))
graphWindow.show()
