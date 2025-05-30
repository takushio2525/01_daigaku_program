import numpy as np
from graph_template import GraphWindow, Graph
import os
import pandas as pd

# プログラムのあるディレクトリ
scriptDir = os.path.dirname(os.path.abspath(__file__))

data = pd.read_csv(os.path.join(scriptDir, "data.csv"))

# 2行1列で全体サイズ指定
# Changed to horizontal layout
graphWindow = GraphWindow(figsize=(15, 5), layout="horizontal")
# graphWindow = GraphWindow(figsize=(15, 15), layout="vertical")  # Changed to vertical layout

g1 = Graph(size_ratio=1, show_grid=True)

# Changed to scatter
g1.add_function(data['売上高 (億円)'], data['1. 接客スコア'], '',
                plot_type="scatter")  # Corrected column name

g1.set_labels(xlabel="売上高 (億円)", ylabel="接客スコア",
              title="売上高と接客スコアの散布図")  # Updated labels
g1.set_range(xlim=(250, 400), ylim=(0, 5))  # Updated ranges


g2 = Graph(size_ratio=1)

# Changed to scatter
g2.add_function(data['売上高 (億円)'], data['2. 品揃えスコア'], '',
                plot_type="scatter")  # Corrected column name

g2.set_labels(xlabel="売上高 (億円)", ylabel="品揃えスコア",
              title="売上高と品揃えスコアの散布図")  # Updated labels
g2.set_range(xlim=(250, 400), ylim=(0, 5))  # Updated ranges

g3 = Graph(size_ratio=1)

# Changed to scatter
g3.add_function(data['売上高 (億円)'], data['3. 立地スコア'], '',
                plot_type="scatter")  # Corrected column name

g3.set_labels(xlabel="売上高 (億円)", ylabel="3. 立地スコア",
              title="売上高と立地スコアの散布図")  # Updated labels
g3.set_range(xlim=(250, 400), ylim=(0, 5))  # Updated ranges


graphWindow.add_graph(g1)
graphWindow.add_graph(g2)
graphWindow.add_graph(g3)


graphWindow.save_all(os.path.join(scriptDir, "g.png"))
# g1を個別に保存する例
graphWindow.save_graph(g1, os.path.join(scriptDir, "g1.png"))
# g2を個別に保存する例
graphWindow.save_graph(g2, os.path.join(scriptDir, "g2.png"))
# g3を個別に保存する例
graphWindow.save_graph(g3, os.path.join(scriptDir, "g3.png"))


# graphWindow.show()
