i = 1
sum = 0

while i <= 100:
    if i == 50:
        continue   # infinite loop!
    sum += i
    i += 1

print(sum)