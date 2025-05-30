import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


class GraphFunction:
    def __init__(self, x, y, label=None, color=None):
        self.x = x
        self.y = y
        self.label = label
        self.color = color


class Graph:
    def __init__(self, subplot_index=None, font_path='/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc', height_ratio=1):
        self.subplot_index = subplot_index  # Noneなら後で自動セット
        self.jp_font = fm.FontProperties(fname=font_path)
        self.functions = []
        self.xlabel = "x"
        self.ylabel = "y"
        self.title = None
        self.xlim = None
        self.ylim = None
        self.semilogy = False
        self.height_ratio = height_ratio  # 縦比のみ
        self.parent_window = None  # 親のGraphWindowを参照

    def add_function(self, x, y, label=None, color=None):
        self.functions.append(GraphFunction(x, y, label, color))

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
            total_height = self.parent_window.figsize[1]
            total_width = self.parent_window.figsize[0]
            height = total_height * \
                (self.height_ratio /
                 sum(g.height_ratio for g in self.parent_window.graphs))
            figsize = (total_width, height)
        else:
            figsize = (8, 6)  # デフォルトサイズ

        fig, ax = plt.subplots(figsize=figsize)
        colors = ["blue", "red", "green", "orange", "purple"]
        for i, func in enumerate(self.functions):
            c = func.color if func.color else colors[i % len(colors)]
            if self.semilogy:
                ax.semilogy(func.x, func.y, label=func.label, color=c)
            else:
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
        ax.grid()
        fig.tight_layout()
        fig.savefig(filename, dpi=300, bbox_inches="tight")
        plt.close(fig)


class GraphWindow:
    def __init__(self, n_subplots=None, font_path='/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc', figsize=(8, 6)):
        self.font_path = font_path
        self.graphs = []
        self.n_subplots = n_subplots  # Noneなら自動決定
        self.figsize = figsize

    def add_graph(self, graph):
        if graph.subplot_index is None:
            graph.subplot_index = len(self.graphs)
        graph.parent_window = self  # Graphに親ウィンドウを設定
        self.graphs.append(graph)

    def show(self):
        n = self.n_subplots if self.n_subplots is not None else len(
            self.graphs)
        height_ratios = [g.height_ratio if hasattr(
            g, 'height_ratio') else 1 for g in self.graphs]
        fig = plt.figure(figsize=self.figsize)
        gs = fig.add_gridspec(n, 1, height_ratios=height_ratios)
        axes = [fig.add_subplot(gs[i, 0]) for i in range(n)]
        colors = ["blue", "red", "green", "orange", "purple"]
        for idx, graph in enumerate(self.graphs):
            ax = axes[graph.subplot_index]
            for i, func in enumerate(graph.functions):
                c = func.color if func.color else colors[i % len(colors)]
                if graph.semilogy:
                    ax.semilogy(func.x, func.y, label=func.label, color=c)
                else:
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
            ax.grid()
        fig.tight_layout()
        plt.show()

    def save_all(self, filename):
        n = self.n_subplots if self.n_subplots is not None else len(
            self.graphs)
        height_ratios = [g.height_ratio if hasattr(
            g, 'height_ratio') else 1 for g in self.graphs]
        fig = plt.figure(figsize=self.figsize)
        gs = fig.add_gridspec(n, 1, height_ratios=height_ratios)
        axes = [fig.add_subplot(gs[i, 0]) for i in range(n)]
        colors = ["blue", "red", "green", "orange", "purple"]
        for idx, graph in enumerate(self.graphs):
            ax = axes[graph.subplot_index]
            for i, func in enumerate(graph.functions):
                c = func.color if func.color else colors[i % len(colors)]
                if graph.semilogy:
                    ax.semilogy(func.x, func.y, label=func.label, color=c)
                else:
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
            ax.grid()
        fig.tight_layout()
        fig.savefig(filename, dpi=300, bbox_inches="tight")
        plt.close(fig)
