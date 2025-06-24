from creature import Creature


# インスタンスの生成
slime1 = Creature("スライム1", 15)
slime2 = Creature("すらすら", 20)

# インスタンスからのメソッドと変数の使用
slime1.getAttacked(slime2.name)
slime2.getDamaged(5)
slime2.getAttacked(slime1.name)
slime1.getDamaged(3)
