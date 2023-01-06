
num = 33
lis = []
i = 1
while i <= num:
    if num % i == 0:
        b = int(num/i)
        j = 1
        k = 0
        while j <= b:
            if b % j == 0:
                k = k +1
            j = j + 1
        if k == 2:
            lis.append(b)
    i = i + 1

print (lis)




