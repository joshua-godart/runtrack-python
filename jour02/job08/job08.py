def job8(type, saison):
    if type=="fruits" and saison =="hiver":
        print("orange, mandarine et kiwi")
    elif type=="fruits" and saison=="été":
        print("poire, fraise, cassis")
    elif type=="légumes" and saison=="hiver":
        print("carotte, topinambour, endive")
    elif type=="légumes" and saison=="été":
        print("artichaut, aubergine, navet")
    else:
        print("non défini")

job8("fruits", "hiver")
job8("légumes", "été")
job8("légumes","hiver")
job8("fruits","automne")