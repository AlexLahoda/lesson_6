list_int = []
ln = int(input("Enter length of the list: "))

for i in range(ln):
    list_int.append(int(input(f"Enter {i} element of the list: ")))

op = int(input("Enter : 1 - reverse, 2 - sort"))
if op == 1:
    print(list(reversed(list_int)))
if op == 2:
    print(sorted(list_int))
