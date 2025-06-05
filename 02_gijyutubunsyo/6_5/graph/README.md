# Graph/GraphWindow テンプレートクラス APIリファレンス

このドキュメントは `graph_template_class.py` のクラス・メソッド・主な引数の解説に特化しています。

---

## Graph クラス

### 概要
- 1つのグラフ（サブプロット）を表現
- データ追加・ラベル・範囲・グリッド・補助線・対数軸など細かく制御可能

### コンストラクタ

#### Graph(
    subplot_index=None,
    font_path='/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc',
    size_ratio=1,
    show_grid=True,
    title_y_offset=None,
    grid_style=None,
    xaxis_line_style=None,
    yaxis_line_style=None,
    show_xaxis_line=True,
    show_yaxis_line=True
)
- **役割**: 1つのグラフ（サブプロット）のインスタンスを生成します。
- **引数**:
    - `subplot_index`: サブプロットのインデックス（自動割当てが基本、省略可）
    - `font_path`: 日本語ラベル・タイトル用フォントパス（macOSデフォルト、省略可）
    - `size_ratio`: 複数グラフ時の相対サイズ比（数値、省略可）
    - `show_grid`: グリッド表示の有無（True/False、省略可）
    - `title_y_offset`: タイトルの縦位置オフセット（数値、省略可）
    - `grid_style`: グリッド線のスタイル辞書（省略可）
    - `xaxis_line_style`, `yaxis_line_style`: x=0, y=0補助線のスタイル辞書（省略可）
    - `show_xaxis_line`, `show_yaxis_line`: x=0, y=0補助線の表示（True/False、省略可）

### 主なメソッド詳細

#### add_function(x, y, label=None, color=None, plot_type="line", linewidth=None, linestyle=None)
- **役割**: グラフにデータ系列（線や点）を追加します。
- **引数**:
    - `x`, `y`: プロットするデータ（リスト、Numpy配列、Pandas Series等）
    - `label`: 凡例ラベル（省略可）
    - `color`: 線や点の色（例: 'blue', '#ff0000' など、省略可）
    - `plot_type`: "line"（折れ線）または "scatter"（散布図）
    - `linewidth`: 線の太さ（折れ線用、省略可）
    - `linestyle`: 線のスタイル（例: '-', '--', ':', 折れ線用、省略可）

#### set_labels(xlabel=None, ylabel=None, title=None, title_y_offset=None)
- **役割**: 軸ラベルやタイトルを設定します。
- **引数**:
    - `xlabel`: x軸ラベル
    - `ylabel`: y軸ラベル
    - `title`: グラフタイトル
    - `title_y_offset`: タイトルの縦位置（デフォルトより上/下にずらしたい場合、省略可）

#### set_range(xlim=None, ylim=None)
- **役割**: x軸・y軸の表示範囲を設定します。
- **引数**:
    - `xlim`: (最小値, 最大値) のタプル、またはNone
    - `ylim`: (最小値, 最大値) のタプル、またはNone

#### set_grid_style(color=None, linestyle=None, linewidth=None, alpha=None, **kwargs)
- **役割**: グリッド線の見た目を細かく調整します。
- **引数**:
    - `color`: グリッド線の色
    - `linestyle`: 線種（例: '-', '--', ':', など）
    - `linewidth`: 線の太さ
    - `alpha`: 透明度（0.0～1.0）
    - `**kwargs`: matplotlibのgridに渡せる他のパラメータ

#### set_xaxis_line_style(**kwargs) / set_yaxis_line_style(**kwargs)
- **役割**: x=0, y=0の補助線の見た目を調整します。
- **引数**:
    - `color`, `linestyle`, `linewidth` など（matplotlibのaxhline/axvlineに準拠）

#### set_xaxis_visibility(show: bool) / set_yaxis_visibility(show: bool)
- **役割**: x=0, y=0の補助線の表示/非表示を切り替えます。
- **引数**:
    - `show`: Trueで表示、Falseで非表示

#### set_semilogy(flag=True)
- **役割**: y軸を対数スケールに切り替えます。
- **引数**:
    - `flag`: Trueで対数軸、Falseで通常軸

#### save(filename)
- **役割**: このグラフ単体を画像ファイルとして保存します。
- **引数**:
    - `filename`: 保存先ファイル名（パス）

---

## GraphWindow クラス

### 概要
- 複数の `Graph` をまとめて1枚の画像やウィンドウに表示
- レイアウトや全体サイズを制御

### コンストラクタ

#### GraphWindow(
    n_subplots=None,
    font_path='/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc',
    figsize=(8, 6),
    layout="vertical",
    width_ratios=None
)
- **役割**: 複数のGraphをまとめて1つのウィンドウや画像として管理・表示します。
- **引数**:
    - `n_subplots`: サブプロット数（省略時は追加されたGraph数で自動決定）
    - `font_path`: 日本語ラベル・タイトル用フォントパス（macOSデフォルト、省略可）
    - `figsize`: 全体のサイズ（(幅, 高さ) のタプル、省略可）
    - `layout`: "vertical"（縦並び）または "horizontal"（横並び）
    - `width_ratios`: 横並び時の各グラフの幅比率（リスト、省略可）

### 主なメソッド詳細

#### add_graph(graph)
- **役割**: グラフ（Graphインスタンス）をウィンドウに追加します。
- **引数**:
    - `graph`: 追加するGraphオブジェクト

#### show()
- **役割**: 追加した全グラフをまとめてmatplotlibウィンドウで表示します。
- **引数**: なし

#### save_all(filename)
- **役割**: 追加した全グラフを1枚の画像ファイルとして保存します。
- **引数**:
    - `filename`: 保存先ファイル名（パス）

#### save_graph(graph, filename)
- **役割**: 指定したグラフのみを個別に画像保存します。
- **引数**:
    - `graph`: 保存したいGraphオブジェクト
    - `filename`: 保存先ファイル名（パス）

---

## GraphFunction（内部クラス）
- `add_function` で自動的に生成されるデータ系列オブジェクト
- `plot_type`, `color`, `linewidth`, `linestyle` などを保持

---

## 備考
- 日本語ラベル・タイトル対応（`font_path`で変更可）
- matplotlib, pandas 必須
- 具体的な使い方は各_exampleのプログラム参照