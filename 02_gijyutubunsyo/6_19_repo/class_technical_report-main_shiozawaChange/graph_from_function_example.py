import numpy as np
from graph_template_class import GraphWindow, Graph
import os
import pandas as pd

# プログラムのあるディレクトリ
scriptDir = os.path.dirname(os.path.abspath(__file__))

# 横並びのレイアウトに変更
# graphWindow = GraphWindow(figsize=(15, 5), layout="horizontal")
# 縦並びのレイアウトに変更
graphWindow = GraphWindow(figsize=(10, 7), layout="vertical")

x1 = np.linspace(-2, 2, 500)
f1 = np.cos(x1)-x1**2



# グラフの定義、全体のうちの比率、グリッドの有無
g1 = Graph()
# 関数を追加
g1.add_function(x1, f1)
g1.set_labels(xlabel="x", ylabel="y")
g1.set_range(xlim=(-2, 2), ylim=(-2, 1.5))



graphWindow.add_graph(g1)


graphWindow.save_all(os.path.join(scriptDir, "func_graph.pdf"))
graphWindow.show()
