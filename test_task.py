def CompareLst(lst1,lst2):
    res_lst = []
    i = 0
    for litera1 in lst1:
        j = 0
        item = {}
        for litera2 in lst2:
            if litera2 == litera1:
                item['litera'] = litera2
                item['found'] = True
                item['shift'] = j - i
                break
            j += 1
        else:
            item['litera'] = litera1
            item['found'] = False
        res_lst.append(item)
        i +=1
    return res_lst

lst1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
lst2 = ['B', 'C', 'D', 'A', 'F', 'E', 'Z', 'M', 'N', 'J', 'K', 'L']
print(lst1)
print(lst2)
res_lst = CompareLst(lst1,lst2)
print("Присутствуют в обоих списках: ")
for item in res_lst:
    if item['found']:
        print(f'Буква: {item["litera"]} с смещением {item["shift"]}')
        if item["shift"] > 0:
            print("смещение влево")
        elif item["shift"] < 0:
            print("смещение вправо")
        else:
            print("нет смещения")
        print()

print("Ушло из списка: ")
for item in res_lst:
    if not item['found']:
        print(item['litera'])

res_lst = CompareLst(lst2,lst1)
print("Добавилось в список: ")
for item in res_lst:
    if not item['found']:
        print(item['litera'])



