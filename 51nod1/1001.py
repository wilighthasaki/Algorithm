params = input()
k = int(params.split()[0])
n = int(params.split()[1])

arr = []

for i in range(n):
    arr.append(int(input()))

# 冒泡排序
# for a in range(n-1):
#     for b in range(0, n-1-a):
#         if arr[b] > arr[b+1]:
#             arr[b], arr[b+1] = arr[b+1], arr[b]


# 快速排序
def quick_sort(testarr , a, b):
    i, j = a, b
    if a < b:
        temp = testarr[i]
        while i < j:
            while testarr[j] > temp and i < j:
                j -= 1
            testarr[i] = testarr[j]
            while testarr[i] < temp and i < j:
                i += 1
            testarr[j] = testarr[i]
        testarr[i] = temp
        quick_sort(testarr, a, i-1)
        quick_sort(testarr, i+1, b)
        return testarr

quick_sort(arr, 0, len(arr)-1)
# print(arr)

start = 0
end = n-1

output = []
while start != end:
    while arr[start] + arr[end] > k and end - start > 1:
        end -= 1
    if arr[start] + arr[end] == k:
        output.append([arr[start], arr[end]])
    if end != start:
        start += 1

if len(output) == 0:
    print('No Solution')
else:
    for i in output:
        print(i[0], i[1])
