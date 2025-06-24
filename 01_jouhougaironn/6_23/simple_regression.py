import numpy as np

class SimpleRegression():
  # コンストラクタを実装
  def __init__(self, x, y):
    # x, yデータを格納
    self.x = x
    self.y = y

    # xとyの平均値を計算して，x_mnとy_mnに格納しておく
    self.x_mn = sum(self.x) / len(self.x)
    self.y_mn = sum(self.y) / len(self.y)

    # x, yの各データと平均値との差分をx_diffおよびy_diffに格納しておく
    self.x_diff = self.x - self.x_mn
    self.y_diff = self.y - self.y_mn

    # hatb1, hatb0 を0で初期化
    self.hatb1 = 0
    self.hatb0 = 0

  # 回帰係数を推定するメソッドを実装

  def estRegCoeff(self):
    # 回帰係数hatb1の推定
    self.hatb1 = np.sum(self.x_diff * self.y_diff) / np.sum(self.x_diff ** 2)
    # 回帰係数hatb0の推定
    self.hatb0 = self.y_mn - self.hatb1 * self.x_mn
    return ([self.hatb0, self.hatb1])

  # 予測値を計算するメソッドを実装
  def predict(self, x):
    # 推定した回帰係数を使用して，引数で受け取った値xの予測値を求める
    haty =  self.hatb0 + self.hatb1 * x
    return (haty)

  # 　決定係数を計算するメソッドを実装
  def calcCoeffDet(self):
    # predictメソッドを使って保持されているデータxの予測値hatyを求める
    haty = self.predict(self.x)
    # SSR, SSE, SSTの計算
    SSR = np.sum((haty - self.y_mn) ** 2)
    SSE = np.sum((self.y - haty) ** 2)
    SST = np.sum((self.y - self.y_mn) ** 2)
    # 　R2の計算
    R2 = SSR / SST
    return ([SSR, SSE, SST, R2])
