class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です。")
        else:
            print(f"{self.name}は大人ではありません。")

# Humanクラスのインスタンスを生成
human1 = Human("侍太郎", 21)
human2 = Human("侍一郎", 19)
human3 = Human("侍花子", 20)
human4 = Human("侍次郎", 10)

# リストに追加
human_list = [human1, human2, human3, human4]

# リストの要素数分だけcheck_adultメソッドを呼び出す
for human in human_list:
    human.check_adult()