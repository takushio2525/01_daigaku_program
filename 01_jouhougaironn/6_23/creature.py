class Creature():
    # コンストラクタの実装
    def __init__(self, name, hp):
        self.name = name  # 名前用の変数
        self.hp = hp      # HP用の変数
        print(self.name, "が現れた！")

    # 攻撃するメソッド
    def getAttacked(self, monster):
        print(self.name, "は" + monster + "を攻撃した！")

    # ダメージを受けるメソッド
    def getDamaged(self, hp):
        self.hp -= hp
        print(self.name, "はHPが" + str(self.hp) + "になった。")
