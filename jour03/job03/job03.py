blacklist=[26, 37, 88]
for x in range(0, 101):
    if x in blacklist:
        continue
    print(x)