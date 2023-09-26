start = int(input("Enter left border of the interval: "))
finish = int(input("Enter right border of the interval: "))

simple_list = []
for i in range(start, finish + 1):
    count = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            count += 1
    if count == 0:
        simple_list.append(i)

print(simple_list)
op = int(input("What would you like to do with it: 1 - sum, 2 - mult ?"))

if op == 1:
    res = sum(simple_list)
elif op == 2:
    mult = 1
    for i in simple_list:
        mult *= i
    res = mult
print(res)
