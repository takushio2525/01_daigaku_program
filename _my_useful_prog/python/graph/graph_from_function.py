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
g1 = Graph(size_ratio=2, show_grid=True)

# 関数を追加
g1.add_function(x1, f1, 'cos(x)-x^2')
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
g1.set_labels(xlabel="x", ylabel="y",
              title="f1 = cos(x) - x^2")
# 範囲を更新
g1.set_range(xlim=(-2, 2), ylim=(-2, 2))
g1.set_grid_style(color='brown', linestyle=(
    0, (4, 2, 1, 2, 1, 2)), linewidth=4, alpha=0.2)


# グラフの定義、全体のうちの比率、グリッドの有無
g2 = Graph(size_ratio=1, show_xaxis_line=False, show_grid=False)

# 関数を追加
g2.add_function(x2, f3, 'fd=-sin(x)-2*x')
# 関数を追加
g2.add_function(x2, f2, 'f=cos(x)-x^2')

# ラベルを更新
g2.set_labels(xlabel="x", ylabel="y",
              title="fとfd")
# 範囲を更新
g2.set_range(xlim=(-2, 2), ylim=(-5, 5))
g2.set_yaxis_line_style(color='green', alpha=0.5,
                        linestyle='dashdot', linewidth=3)
g3 = Graph(size_ratio=1)


graphWindow.add_graph(g1)
graphWindow.add_graph(g2)


graphWindow.save_all(os.path.join(scriptDir, "csv_graph.png"))
# # g1を個別に保存する例
graphWindow.save_graph(g1, os.path.join(scriptDir, "g1.png"))
# # g2を個別に保存する例
# graphWindow.save_graph(g2, os.path.join(scriptDir, "g2.png"))
# # g3を個別に保存する例
# graphWindow.save_graph(g3, os.path.join(scriptDir, "g3.png"))


graphWindow.show()
