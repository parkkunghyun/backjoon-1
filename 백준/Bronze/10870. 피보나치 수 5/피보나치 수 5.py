n = int(input())

def recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive(n-1) + recursive(n-2)

print(recursive(n))