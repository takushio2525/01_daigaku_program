import numpy as np
from graph_template_class import GraphWindow, Graph
import os
import pandas as pd

# プログラムのあるディレクトリ
scriptDir = os.path.dirname(os.path.abspath(__file__))

data = pd.read_csv(os.path.join(scriptDir, "data.csv"))

# 全体のサイズとレイアウトを指定
graphWindow = GraphWindow(figsize=(15, 5), layout="horizontal")  # 横並びのレイアウト
# graphWindow = GraphWindow(figsize=(15, 15), layout="vertical")  # 縦並びのレイアウト


# グラフの定義
# 1つ目
g1 = Graph()
g1.add_function(data['売上高 (億円)'], data['1. 接客スコア'], plot_type="scatter")
g1.set_labels(xlabel="売上高 (億円)", ylabel="接客スコア", title="売上高と接客スコアの散布図")
g1.set_range(xlim=(250, 400), ylim=(0, 5))

# 2つ目
g2 = Graph()
g2.add_function(data['売上高 (億円)'], data['2. 品揃えスコア'], plot_type="scatter")
g2.set_labels(xlabel="売上高 (億円)", ylabel="品揃えスコア", title="売上高と品揃えスコアの散布図")
g2.set_range(xlim=(250, 400), ylim=(0, 5))

# 3つ目
g3 = Graph()
g3.add_function(data['売上高 (億円)'], data['3. 立地スコア'], plot_type="scatter")
g3.set_labels(xlabel="売上高 (億円)", ylabel="3. 立地スコア", title="売上高と立地スコアの散布図")
g3.set_range(xlim=(250, 400), ylim=(0, 5))


graphWindow.add_graph(g1)
graphWindow.add_graph(g2)
graphWindow.add_graph(g3)

# graphWindow.save_all(os.path.join(scriptDir, "csv_graph.png"))
# # g1を個別に保存する例
# graphWindow.save_graph(g1, os.path.join(scriptDir, "g1.png"))
# # g2を個別に保存する例
# graphWindow.save_graph(g2, os.path.join(scriptDir, "g2.png"))
# # g3を個別に保存する例
# graphWindow.save_graph(g3, os.path.join(scriptDir, "g3.png"))


graphWindow.show()
