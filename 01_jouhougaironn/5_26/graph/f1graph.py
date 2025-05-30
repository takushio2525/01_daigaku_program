import numpy as np
from graph_template import GraphWindow, Graph
import os


# プログラムのあるディレクトリ
scriptDir = os.path.dirname(os.path.abspath(__file__))

# ウィンドウを用意
graphWindow = GraphWindow(figsize=(10, 8))

# x軸データ
x = np.linspace(-2, 2, 500)

f = np.cos(x) - x**2


g1 = Graph()
g1.add_function(x, f)
g1.set_labels(xlabel="x", ylabel="y")

graphWindow.add_graph(g1)

# g1.save(os.path.join(scriptDir, "f1.png"))
graphWindow.save_all(os.path.join(scriptDir, "f1.png"))
graphWindow.show()
