n, m = map(int, input().split())

def lcm(a, b):
    for i in range(1, a):
        num = i * a
        if num % b == 0:
            return num
    return a * b

print(lcm(n,m))