now = int(input())
maxNum = now
while now != 0:
    now = int(input())
    if now == 0:
        break
    if now > maxNum:
        maxNum = now
print(maxNum)
