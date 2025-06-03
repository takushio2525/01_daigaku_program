import numpy as np
from graph_template_class import GraphWindow, Graph
import os

# データ生成
x = np.linspace(-5, 5, 200)
y1 = np.sin(x)
y2 = np.cos(x)

# グラフ定義（全ての主要な引数を明示的に指定）
g = Graph(
    size_ratio=1.5,
    show_grid=True,
    font_path='/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc',
    title_y_offset=0.8,
    grid_style={'color': 'orange', 'linestyle': ':',
                'linewidth': 2, 'alpha': 0.5},
    xaxis_line_style={'color': 'red', 'linewidth': 2, 'linestyle': '--'},
    yaxis_line_style={'color': 'blue', 'linewidth': 2, 'linestyle': '-.'},
    show_xaxis_line=True,
    show_yaxis_line=True
)

# 折れ線グラフ（色・線種・太さ指定）
g.add_function(x, y1, label='sin(x)', color='green',
               plot_type='line', linewidth=3, linestyle='--')
# 散布図（色・点の太さ指定）
g.add_function(x, y2, label='cos(x)', color='purple',
               plot_type='scatter', linewidth=2)

g.set_labels(xlabel='x軸', ylabel='y軸', title='sinとcosの例', title_y_offset=1.1)
g.set_range(xlim=(-5, 5), ylim=(-1.5, 1.5))
g.set_semilogy(False)

graphWindow = GraphWindow(
    n_subplots=1,
    font_path='/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc',
    figsize=(8, 4),
    layout='horizontal',
    width_ratios=[1]
)
graphWindow.add_graph(g)

# 保存と表示1
scriptDir = os.path.dirname(os.path.abspath(__file__))
#graphWindow.save_all(os.path.join(scriptDir, 'all_example.png'))
graphWindow.show()