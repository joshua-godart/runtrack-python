def tri(a, b, c):
    if a<=b+c and b<=a+c and c<=a+b:
        print("construtible")
        if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
            print("triangle rectangle")
        elif a==b==c:
            print("triangle équilatéral")
        elif a**2==2*b**2 or b**2==2*a**2 or c**2==2*b**2:
            print("triangle rectangle isocèle")
        elif a==b!=c or a==c!=b or b==c!=a:
            print("triangle isocèle")
        else:
            print("triangle quelconque")

    else:
        print("non constructible")
    


tri(5, 5, 5 )
tri(8, 12, 7)
tri(8, 6, 10)
tri(5, 5, 8)