import math

b = float(input('введите точность округления ' ))
a = math.pi
i = 0
while b < 1:
    b = b * 10
    i = i+1
print (round(a,i))