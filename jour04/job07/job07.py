L=[8, 24, 48, 2, 16]
compte=0
for i in L:
    if i % 3 == 0:
        compte += 1
print(compte)


x= sum([1 for num in L if num % 3 == 0])
print(x)
