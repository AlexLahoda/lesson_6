int_list = input("Enter natural numbers separated by commas: ").split(',')
new_lst = []
for i in int_list:
    if int(i) % 2 != 0:
        new_lst.append(i)
rep = int(input("How much times do you want to repeat it: "))
new_lst *= rep
print(new_lst)
int_list.clear()
