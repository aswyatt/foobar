def solution(s):
    N = len(s)

    #  Need at least 2 people
    if N<2:
        return 0

    #   Initialisation
    #   Number of consecutive henchmen moving right/left
    right = []
    left = []

    #   Last Henchman
    lastDir = ">"

    #   Number of consecutive henchmen
    count = 0
    for pos in range(N):
        #   Current character
        c = s[pos]

        #   Check for henchman
        if c in "<>":
            if c is lastDir:
                #   Current & last henchman moving in same direction
                count += 1
            else:
                #   Change of henchman direction, update arrays & change direction flag
                if lastDir == ">":
                    right.append(count)
                    lastDir = "<"
                else:
                    left.append(count)
                    lastDir = ">"
                count = 1

    #   Append # of left henchmen
    if lastDir == "<":
        left.append(count)

    #   Sum number of salutes
    count = 0
    for nr in range(len(right)):
        for nl in range(nr, len(left)):
            count += right[nr] * left[nl]

    #   Total is twice the count
    return 2*count

s = "<<-->>-<->"
print(s + ":", solution(s))

s = "--->-><-><-->-"
print(s + ":", solution(s))

s = ">----<"
print(s + ":", solution(s))

s = "<<>><"
print(s + ":", solution(s))

# a = []
# b = []
# print("a:", a)
# print("b:", b)
# c = a
# c.append(1)
# print("a:", a)
# print("b:", b)
# print("c:", c)
