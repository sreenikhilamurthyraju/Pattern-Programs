for x in range(1,16):
    for y in range(1,11):
        if(((x>=4 or x<=6) and y>=4) or ((x>=10 and x<=12) and (y<=7))):
            print("", end="")
        else:
            print("*", end="")
    print()

