list_1 = input(
    "Enter elements of the first list, separated by a comma: ").split(',')
list_2 = input(
    "Enter elements of the second list, separated by a comma: ").split(',')
list_1.extend(list_2)
sym_dif = []
for i in list_1:
    if i not in sym_dif:
        sym_dif.append(i)
print(sym_dif)
print(list(reversed(sym_dif)))
print(sorted(sym_dif))
print(sorted(sym_dif, reverse=True))
