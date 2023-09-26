from five import new_lst

num = input("Enter your value: ")


indxs = []
for i in range(len(new_lst)):
    if new_lst[i] == num:
        indxs.append(i)
print(
    f" There is {new_lst.count(num)} such values in the list, and it's position is {indxs}")
