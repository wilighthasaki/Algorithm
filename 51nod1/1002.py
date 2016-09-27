N = int(input())
total_arr = []
for _ in range(N):
    temp_arr = input().split()
    arr = [int(num) for num in temp_arr]
    total_arr.append(arr)

max_route = [[0 for _ in range(i+1)] for i in range(N)]

for i in range(N):
    for j in range(i+1):
        if j == 0:
            max_route[i][j] = max_route[i-1][j] + total_arr[i][j]
        elif j == i:
            max_route[i][j] = max_route[i-1][j-1] + total_arr[i][j]
        else:
            max_route[i][j] = (max_route[i-1][j] if max_route[i-1][j] > max_route[i-1][j-1] else max_route[i-1][j-1]) + total_arr[i][j]

max = 0

for i in range(N):
    if max < max_route[N-1][i]:
        max = max_route[N-1][i]
print(max)
