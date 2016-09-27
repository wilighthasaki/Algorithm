a = [i for i in range(12)]
a.extend([i for i in range(6, 3, -1)])

print(a)

def get_top(n, m):
    if n == m :
        return a[n]
    elif a[int((n + m)/2)] > a[int((n + m)/2) + 1]:
        return get_top(n, int((n + m)/2))
    else:
        return get_top(int((n + m)/2) + 1, m)


print(get_top(0, len(a)-1))
