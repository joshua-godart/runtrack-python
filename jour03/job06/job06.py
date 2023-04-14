alph="abcdefghijklmnopqrstuvwxyz" * 10

i=1

while i <= len(alph):
    print(alph[:i])
    alph=alph[i:]
    i+=1
