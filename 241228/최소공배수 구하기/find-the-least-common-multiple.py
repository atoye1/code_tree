n, m = map(int, input().split())

def lcm(a, b):
    if a > b:
        a, b = b, a
    for i in range(1, a + 1):
        num = i * a
        if num % b == 0:
            return num
    return a * b

print(lcm(n,m))