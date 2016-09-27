num = int(input())

devidend = 5
count = 0

while devidend <= num :
    count += int(num/devidend)
    devidend *= 5
print(count)