a = 6
b = 3
c = 5
d = 4
list_a = [a,b,c,d]


i = 0
for i in range(len(list_a)):
    i += 1
    m = 0
    for m in range(len(list_a)):
        if m + 1 < len(list_a):
            item_1 = list_a[m]
            item_2 = list_a[m + 1]
            if item_1 > item_2:
                list_a[m] = item_2
                list_a[m + 1] = item_1
                m += 1
                print(list_a)
                print(f'{m} 2')
            else:
                m += 1




