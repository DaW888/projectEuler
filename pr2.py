prev, cur = 0, 1
sum = 0

while cur <= 4e6:
    prev, cur = cur, prev + cur
    print(cur)
    if cur % 2 == 0:
        sum += cur

print('suma')
print(sum)