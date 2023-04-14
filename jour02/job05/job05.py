def calcul(num1, operator, num2):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="/":
        return num1/num2
    elif operator=="*":
        return num1*num2
    elif operator=="%":
        return num1%num2
    else:
        return "wrong"

print(calcul(10, "+", 15))
print(calcul(25,"-", 15))
print(calcul(25,"/",5))
print(calcul(5,"*",5))
print(calcul(5,"%",5))
print(calcul(5,"pp",5))