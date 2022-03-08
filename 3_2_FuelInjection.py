def solution(n):
    #   Convert to integer and start search
    return search(eval(n))

def power_of_2(n):
    return not(n & (n-1))

def isOdd(n):
    return (n % 2)

def isEven(n):
    return not isOdd(n)

#   Modify value until it reaches 1 and count number of modifications
def search(n):
    count = 0
    while n>1:
        if isEven(n):
            #   This will always return an odd value for n
            (n, c) = searchEven(n)
            count += c
        #   Guaranteed odd, so search it
        (n, c) = searchOdd(n)
        count += c
    #   Return the result
    return count

#   Count number of halvings until odd value found
def searchEven(n):
    #   Check for direct answer
    if power_of_2(n):
        return (1, n.bit_length()-1)

    #   Not power of 2, so half until odd
    count = 0
    while isEven(n):
        n = n>>1
        count +=1
    return (n, count)

#   Need to increment or decrement by 1 and then half
def searchOdd(n):
    #   Due to logic above, need to check if input = 1
    if n==1:
        return (1, 0)

    #   Find next lowest odd number and number of halvings
    np, cp = searchEven(n+1)
    nm, cm = searchEven(n-1)
    if (np==1 and nm==1):
        #   Both returned 1, return lowest count
        return (1, 1+min(cp, cm))
    elif (np==nm):
        #   Both returned same value, return lowest count
        return (np, 1+min(cp, cm))
    elif (np<nm):
        #   search of n+1 returned lowest number
        return (np, 1+cp)
    else:
        #   search of n-1 returned lowest number
        return (nm, 1+cm)

# def search(n):
#     bits = n.bit_length()
#     if power_of_2(n):
#         #   Is power of 2, so return 1 less
#         return bits-1
#     if (n % 2):
#         #   Number is odd, so need to add or subtract 1
#         if power_of_2(n-1):
#             #   Increment by 1 to reach power of 2
#             return bits
#         elif power_of_2(n+1):
#             #   Decrement by 1 to reach power of 2
#             return bits + 1
#         else:
#             #   Decrement by 1 then half
#             return 2 + min(search((n-1)>>1), search((n+1)>>1))
#     else:
#         #   Number is odd, so half it
#         return 1 + search(n>>1)

# def search(n):
#     #   Initialise counter
#     count = 0
#     while n>1:
#         #   Get log2(next power of 2)
#         bits = n.bit_length()
#         if power_of_2(n):
#             #   Is power of 2, so return 1 less
#             return count + bits-1
#         if (n % 2):
#             #   Number is odd, so need to add or subtract 1
#             if power_of_2(n-1):
#                 #   Increment by 1 to reach power of 2
#                 return count + bits
#             elif power_of_2(n+1):
#                 #   Decrement by 1 to reach power of 2
#                 return count + bits + 1
#             else:
#                 return 2 + min(search((n-1)>>1), search((n+1)>>1))
#                 # if (3*(1<<(bits-2))<n):
#                 #     #   Increment by 1 then half
#                 #     n += 1
#                 # else:
#                 #     #   Decrement by 1 then half
#                 #     n -= 1
#                 # n = (n>>1)
#                 # count += 2
#         else:
#             #   Number is odd, so half it
#             n = (n>>1)
#             count +=1
#     #   Reached n=1, so return count
#     return count

# def search(n):
#     #  Almost works
#     if n==1:
#         return 0
#     #   Get length of bits (for finding 2^bits)
#     bits = n.bit_length()
#     #   Distance from 2^bits
#     if ((1<<(bits-1))-n)==0:
#         return bits-1
#     elif (n % 2):
#         if (n-(1<<(bits-1)))==1:
#             return bits
#         elif ((1<<bits)-n)==1:
#             return bits+1
#         else:
#             #   Move +/- 1 step
#             return 1+min(solution(n-1), solution(n+1))
#     else:
#         #   Return solution for half number
#         return 1+solution(n//2)

def PRINT(n):
    print(str(n) + ": " + str(solution(str(n))))

# n = 9
# print(str(n) + ": " + str(solution(str(n))))
# for n in range(3, 20):
    # PRINT(n)

import random
N = 100
s = str(random.randint(1,9))
for n in range(N):
    s += str(random.randint(0, 9))
PRINT(s)
