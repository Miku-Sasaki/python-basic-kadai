def calculate_trapezoid_area(upper_base, lower_base, height):
    """
    台形の面積を計算する関数
    公式：(上辺 + 下辺) * 高さ / 2
    """
    area = (upper_base + lower_base) * height / 2
    return area

# 変数の設定
upper = 10
lower = 20
h = 5

# 関数の呼び出し
result = calculate_trapezoid_area(upper, lower, h)

# 結果の出力
print(f"{result}cm2")