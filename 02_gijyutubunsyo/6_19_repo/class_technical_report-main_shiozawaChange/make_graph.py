import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Load the data
scriptDir = os.path.dirname(os.path.abspath(__file__))

bi_result = pd.read_csv(os.path.join(scriptDir, "bi_result2.csv"), header=None)
new_result = pd.read_csv(os.path.join(scriptDir, "new_result2.csv"), header=None)

# bi_result = pd.read_csv("bi_result2.csv", header=None)
# new_result = pd.read_csv("new_result2.csv", header=None)

# Configure the plotting environment
# 日本語フォントを設定
jp_font = fm.FontProperties(fname='/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc')
#plt.rcParams['font.family'] = jp_font.get_name()

plt.rcParams.update({
    'font.family': jp_font.get_name(),
    'font.size': 25,
    'axes.labelsize': 25,
    'axes.titlesize': 25
})

# Create the figure
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# First subplot
axs[0].plot(bi_result.iloc[:, 0], bi_result.iloc[:, 2], '-b', linewidth=2, label='二分法')
axs[0].plot(new_result.iloc[:, 0], new_result.iloc[:, 2], '-r', linewidth=2, label='ニュートン法')
axs[0].set_xlabel("繰り返し回数: $n$")
axs[0].set_ylabel("推定解: $x_n$")
axs[0].legend()
axs[0].grid(True)

# Second subplot
axs[1].semilogy(bi_result.iloc[:, 0], bi_result.iloc[:, 1], '-b', linewidth=2, label='二分法')
axs[1].semilogy(new_result.iloc[:, 0], new_result.iloc[:, 1], '-r', linewidth=2, label='ニュートン法')
axs[1].set_xlabel("繰り返し回数: $n$")
axs[1].set_ylabel("誤差: $|x_{n-1} - x_n|$")
axs[1].legend()
axs[1].grid(True)

# Display the plot
plt.tight_layout()
# plt.savefig(os.path.join(scriptDir, "comparison_plot.pdf"))
plt.show()
