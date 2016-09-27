num = int(input())


single = num % 10
if single == 0:
    print(0)
else:
    result = single ** (num % 4) % 10
    print(result)