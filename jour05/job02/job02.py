
def rectangle(L, C):
    for i in range(1, L+1):
        for j in range(1, C+1):
            if j == 1 or j == C:
                print("| ", end="")
            elif i == 1 or i == L:
                print("- ", end="")
            else:
                print("  ", end="")
        print()
rectangle(3, 10)