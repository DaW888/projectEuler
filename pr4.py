maxMulti = 0
max1 = 0
max2 = 0
for i in range(900, 1000):
    for j in range(900, 1000):
        multi = i*j
        multiTxt = str(multi)

        part1 = multiTxt[:len(str(i))]
        part2 = multiTxt[len(str(i)):]
        part2 = part2[::-1]

        if part1 == part2:
            if multi > maxMulti:
                maxMulti = multi
                max1 = i
                max2 = j
print(maxMulti, max1, max2)