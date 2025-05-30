import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


class GraphFunction:
    def __init__(self, x, y, label=None, color=None, plot_type="line"):  # Added plot_type
        self.x = x
        self.y = y
        self.label = label
        self.color = color
        self.plot_type = plot_type  # Added plot_type


class Graph:
    # Changed height_ratio to size_ratio
    def __init__(self, subplot_index=None, font_path='/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc', size_ratio=1, show_grid=True):  # Added show_grid
        self.subplot_index = subplot_index  # Noneなら後で自動セット
        self.jp_font = fm.FontProperties(fname=font_path)
        self.functions = []
        self.xlabel = "x"
        self.ylabel = "y"
        self.title = None
        self.xlim = None
        self.ylim = None
        self.semilogy = False
        self.size_ratio = size_ratio  # Changed height_ratio to size_ratio
        self.parent_window = None  # 親のGraphWindowを参照
        self.show_grid = show_grid  # Added show_grid

    def add_function(self, x, y, label=None, color=None, plot_type="line"):  # Added plot_type
        self.functions.append(GraphFunction(
            x, y, label, color, plot_type))  # Pass plot_type

    def set_labels(self, xlabel=None, ylabel=None, title=None):
        if xlabel:
            self.xlabel = xlabel
        if ylabel:
            self.ylabel = ylabel
        if title:
            self.title = title

    def set_range(self, xlim=None, ylim=None):
        self.xlim = xlim
        self.ylim = ylim

    def set_semilogy(self, flag=True):
        self.semilogy = flag

    def save(self, filename):
        # 親ウィンドウのfigsizeを基に個別のfigsizeを計算
        if self.parent_window:
            parent_fig_width, parent_fig_height = self.parent_window.figsize
            num_graphs_in_window = len(self.parent_window.graphs)

            if self.parent_window.layout == "horizontal":
                # 水平レイアウトの場合
                # 高さは親ウィンドウの高さを使用
                height = parent_fig_height

                # 幅は、親ウィンドウの総幅をsize_ratioに基づいて按分
                total_size_ratio = sum(
                    g.size_ratio for g in self.parent_window.graphs if hasattr(g, 'size_ratio'))
                if total_size_ratio > 0 and num_graphs_in_window > 0:
                    # このグラフのsize_ratioが全体のsize_ratio合計に占める割合で幅を決定
                    width = parent_fig_width * \
                        (self.size_ratio / total_size_ratio)
                else:
                    # フォールバック: 等分
                    width = parent_fig_width / \
                        num_graphs_in_window if num_graphs_in_window > 0 else parent_fig_width

                current_figsize = (width, height)

            else:  # Vertical layout
                # 垂直レイアウトの場合
                # 幅は親ウィンドウの幅を使用
                width = parent_fig_width

                # 高さは、親ウィンドウの総高さをsize_ratioに基づいて按分
                total_size_ratio = sum(
                    g.size_ratio for g in self.parent_window.graphs if hasattr(g, 'size_ratio'))
                if total_size_ratio > 0 and num_graphs_in_window > 0:
                    height = parent_fig_height * \
                        (self.size_ratio / total_size_ratio)
                else:
                    # フォールバック: 等分
                    height = parent_fig_height / \
                        num_graphs_in_window if num_graphs_in_window > 0 else parent_fig_height

                current_figsize = (width, height)
        else:
            # 親ウィンドウがない場合 (Graph単体でsaveを呼んだ場合)
            current_figsize = (8, 6)  # デフォルトのfigsize

        fig, ax = plt.subplots(figsize=current_figsize)
        colors = ["blue", "red", "green", "orange", "purple"]
        for i, func in enumerate(self.functions):
            c = func.color if func.color else colors[i % len(colors)]
            if self.semilogy:
                # semilogy for scatter is not explicitly handled here, assuming line for semilogy
                ax.semilogy(func.x, func.y, label=func.label, color=c)
            else:
                if func.plot_type == "scatter":
                    ax.scatter(func.x, func.y, label=func.label, color=c)
                else:  # Default to line plot
                    ax.plot(func.x, func.y, label=func.label, color=c)
        ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
        ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
        ax.set_xlabel(self.xlabel, fontproperties=self.jp_font)
        ax.set_ylabel(self.ylabel, fontproperties=self.jp_font)
        if self.xlim:
            ax.set_xlim(self.xlim)
        if self.ylim:
            ax.set_ylim(self.ylim)
        if self.title:
            ax.set_title(self.title, fontproperties=self.jp_font)
        if any(func.label for func in self.functions):
            ax.legend(prop=self.jp_font)
        if self.show_grid:  # Added condition for grid
            ax.grid()
        fig.tight_layout()
        fig.savefig(filename, dpi=300, bbox_inches="tight")
        plt.close(fig)


class GraphWindow:
    def __init__(self, n_subplots=None, font_path='/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc', figsize=(8, 6), layout="vertical", width_ratios=None):  # Added layout and width_ratios
        self.font_path = font_path
        self.graphs = []
        self.n_subplots = n_subplots  # Noneなら自動決定
        self.figsize = figsize
        self.layout = layout  # Added layout
        self.width_ratios = width_ratios  # Added width_ratios

    def add_graph(self, graph):
        if graph.subplot_index is None:
            graph.subplot_index = len(self.graphs)
        graph.parent_window = self  # Graphに親ウィンドウを設定
        self.graphs.append(graph)

    def show(self):
        n = self.n_subplots if self.n_subplots is not None else len(
            self.graphs)

        fig = plt.figure(figsize=self.figsize)

        if self.layout == "vertical":
            height_ratios = [g.size_ratio if hasattr(
                g, 'size_ratio') else 1 for g in self.graphs]
            gs = fig.add_gridspec(n, 1, height_ratios=height_ratios)
            axes = [fig.add_subplot(gs[i, 0]) for i in range(n)]
        elif self.layout == "horizontal":
            # Use size_ratio for width_ratios if self.width_ratios is not provided
            if self.width_ratios:
                width_ratios = self.width_ratios
            else:
                width_ratios = [g.size_ratio if hasattr(
                    g, 'size_ratio') else 1 for g in self.graphs]
            gs = fig.add_gridspec(1, n, width_ratios=width_ratios)
            axes = [fig.add_subplot(gs[0, i]) for i in range(n)]
        else:
            raise ValueError("Layout must be 'vertical' or 'horizontal'")

        colors = ["blue", "red", "green", "orange", "purple"]
        for idx, graph in enumerate(self.graphs):
            ax = axes[graph.subplot_index]
            for i, func in enumerate(graph.functions):
                c = func.color if func.color else colors[i % len(colors)]
                if graph.semilogy:
                    # semilogy for scatter is not explicitly handled here, assuming line for semilogy
                    ax.semilogy(func.x, func.y, label=func.label, color=c)
                else:
                    if func.plot_type == "scatter":
                        ax.scatter(func.x, func.y, label=func.label, color=c)
                    else:  # Default to line plot
                        ax.plot(func.x, func.y, label=func.label, color=c)
            ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
            ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
            ax.set_xlabel(graph.xlabel, fontproperties=graph.jp_font)
            ax.set_ylabel(graph.ylabel, fontproperties=graph.jp_font)
            if graph.xlim:
                ax.set_xlim(graph.xlim)
            if graph.ylim:
                ax.set_ylim(graph.ylim)
            if graph.title:
                ax.set_title(graph.title, fontproperties=graph.jp_font)
            if any(func.label for func in graph.functions):
                ax.legend(prop=graph.jp_font)
            if graph.show_grid:  # Added condition for grid
                ax.grid()
        fig.tight_layout()
        plt.show()

    def save_all(self, filename):
        n = self.n_subplots if self.n_subplots is not None else len(
            self.graphs)

        fig = plt.figure(figsize=self.figsize)

        if self.layout == "vertical":
            height_ratios = [g.size_ratio if hasattr(
                g, 'size_ratio') else 1 for g in self.graphs]
            gs = fig.add_gridspec(n, 1, height_ratios=height_ratios)
            axes = [fig.add_subplot(gs[i, 0]) for i in range(n)]
        elif self.layout == "horizontal":
            # Use size_ratio for width_ratios if self.width_ratios is not provided
            if self.width_ratios:
                width_ratios = self.width_ratios
            else:
                width_ratios = [g.size_ratio if hasattr(
                    g, 'size_ratio') else 1 for g in self.graphs]
            gs = fig.add_gridspec(1, n, width_ratios=width_ratios)
            axes = [fig.add_subplot(gs[0, i]) for i in range(n)]
        else:
            raise ValueError("Layout must be 'vertical' or 'horizontal'")

        colors = ["blue", "red", "green", "orange", "purple"]
        for idx, graph in enumerate(self.graphs):
            ax = axes[graph.subplot_index]
            for i, func in enumerate(graph.functions):
                c = func.color if func.color else colors[i % len(colors)]
                if graph.semilogy:
                    # semilogy for scatter is not explicitly handled here, assuming line for semilogy
                    ax.semilogy(func.x, func.y, label=func.label, color=c)
                else:
                    if func.plot_type == "scatter":
                        ax.scatter(func.x, func.y, label=func.label, color=c)
                    else:  # Default to line plot
                        ax.plot(func.x, func.y, label=func.label, color=c)
            ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
            ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
            ax.set_xlabel(graph.xlabel, fontproperties=graph.jp_font)
            ax.set_ylabel(graph.ylabel, fontproperties=graph.jp_font)
            if graph.xlim:
                ax.set_xlim(graph.xlim)
            if graph.ylim:
                ax.set_ylim(graph.ylim)
            if graph.title:
                ax.set_title(graph.title, fontproperties=graph.jp_font)
            if any(func.label for func in graph.functions):
                ax.legend(prop=graph.jp_font)
            if graph.show_grid:  # Added condition for grid
                ax.grid()
        fig.tight_layout()
        fig.savefig(filename, dpi=300, bbox_inches="tight")
        plt.close(fig)

    def save_graph(self, graph_to_save, filename):
        """
        ウィンドウに追加された特定のグラフオブジェクトをファイルに保存します。
        """
        if graph_to_save in self.graphs:
            # Graphオブジェクト自身のsaveメソッドを呼び出す
            # これにより、Graphオブジェクトが持つfigsize計算ロジックが利用される
            graph_to_save.save(filename)
        else:
            print(f"Error: The specified graph is not part of this GraphWindow.")
