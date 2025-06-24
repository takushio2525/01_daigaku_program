from simple_regression import SimpleRegression
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

scriptDir = os.path.dirname(os.path.abspath(__file__))

# ファイルからデータを読み込む osでファイルのパスを指定
file_path = os.path.join(scriptDir, "practice.csv")
df = pd.read_csv(file_path)

# データを変数に格納
x = df["x"].values
y = df["y"].values


# 格納されているか確認
print("x = ", x)
print("y = ", y)

reg = SimpleRegression(x, y)

# 回帰係数hatb0, hatb1を求める
[hatb0, hatb1] = reg.estRegCoeff()
print("hatb0 = ", hatb0)
print("hatb1 = ", hatb1)


# 予測値を求める
haty = reg.predict(x)
print("haty = ", haty)

# 決定係数を求める
R2 = reg.calcCoeffDet()
print("SSR = ", np.round(R2[0], 2))
print("SSE = ", np.round(R2[1], 2))
print("SST = ", np.round(R2[2], 2))
print("R2 = ", np.round(R2[3], 2))

fig, ax = plt.subplots()
# x,y軸を同じサイズで描くおまじない
ax.set_aspect('equal', 'box')

# 　軸の設定
ax.set_xlim([0, 7])
ax.set_ylim([7, 14])
ax.set_xticks(np.arange(0, 7))
ax.set_yticks(np.arange(7, 14))
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)
ax.tick_params(labelsize=14)
ax.grid()

# 　xとyの散布図を描く
ax.scatter(x, y, marker='o', color='blue', label='data')
# x軸の値を取得
xticks = ax.get_xticks()
# x軸の値に対する予測値を取得
haty4xticks = reg.predict(xticks)
# 回帰直線を引く
ax.plot(xticks, haty4xticks, color='red', label='regression line')

plt.tight_layout()
# ファイルに書き出し
plt.savefig(os.path.join(scriptDir, "worksheet.pdf"), dpi=300)
