lis = [1,2,2,3,4,4,5,6,77,7,7]
lis_res = []

for num in lis:
    i = 0
    k = 0
    while i <= len(lis)-1:
        if num == lis[i]:
            k = k + 1
        i = i + 1
    if k == 1:
        lis_res.append(num)
print (lis_res)
