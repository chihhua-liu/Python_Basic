from fractions import Fraction  # (分數可通分)

a1 = Fraction(250, 72)
print(a1)
a2 = Fraction(200, 80)
a3 = a1 + a2
print(a3)
print(a3.numerator)     # 分子
print(a3.denominator)   # 分母