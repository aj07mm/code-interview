# 1 1 2 3 5 8 13
# 1 2 3 4 5 6 7

#def fib(n):
#    if n < 2:
#        return n
#    return fib(n-1) + fib(n-2)
#
#print(fib(7))

# 7
# fib(7-1) + fib(7-2)
# fib(6-1) + fib(6-2) + fib(5-1) + fib(5-2)
# fib(5-1) + fib(5-2) + fib(4-1) + fib(4-2) + fib(3-1) + fib(3-2)


# 13 -> [1, 1, 2, 3, 5, 8, 13]
#        0  1  2  3  4  5  6    
    
def fib_range(n):
    acc = [1, 1]
    for n in range(2, n+1):
        acc.append(acc[-1]+acc[-2])
    return acc

print(fib_range(4))



