def solution(M, F):
    #   Extract initial bomb values
    M = eval(M.replace("^", "**"))
    F = eval(F.replace("^", "**"))

    #   Initialise generation counter
    gen = 0

    #   Decrease M, F until any(M,F)<=1
    while ((M>0) and (F>0)):
        #   Found solution
        if M==1:
            return str(gen + F-1)
        if F==1:
            return str(gen + M-1)

        #   Since M+F > all(M,F), find M' = M-nF or F' = F-nM at each step
        if (M>F):
            M, n = update(M, F)
        else:
            F, n = update(F, M)
        gen+=n
    return "impossible"

def update(a, b):
    #   Note: a>b
    n = (a//b)
    a = a-b*n
    return (a, n)

print(solution("1", "1"), "\n")
print(solution("2", "1"), "\n")
print(solution("4", "7"), "\n")
print(solution("2", "4"), "\n")
print(solution("10^50", "100"))