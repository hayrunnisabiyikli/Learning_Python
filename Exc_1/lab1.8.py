"""height = 5
for row in range(1, height + 1):
    spaces_before_star = abs(row - (height // 2 + 1))
    stars = height - spaces_before_star * 2
    for i in range(spaces_before_star):
        print(" ", end="")
    for i in range(stars):
        print("*", end="")
    print()"""


for i in range(3):
    for k in range((3)-i):
        print("",end="")
    for m in range((i*2)-1):
            print("*", end="")
            print()
    for i in range(3,0,-1):
        for k in range((3)-i):
            print("",end="")
        for m in range((i*2)-1):
            print("*",end="")
            print()
