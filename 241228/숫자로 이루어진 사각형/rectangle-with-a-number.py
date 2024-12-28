N = int(input())
count = 1
for i in range(N):
    for j in range(N):
        print(count, end = ' ')
        count += 1
        if count == 10:
            count = 1
    print()