# with open('data.txt', encoding='utf-8') as file:
#     cook_book = {}
#     for i in file:
#         recepie_name = i.strip()
#         ingredients_count = file.readline()
#         ingredients = []
#         for p in range(int(ingredients_count)):
#             recepie = file.readline().strip().split(' | ')
#             product, quantity, word = recepie
#             ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
#         file.readline()
#         cook_book[recepie_name] = ingredients
#     # print(cook_book)
#
# def get_shop_list_by_dishes(person_count: int, dishes: list):
#     result = {}
#     for dish in dishes:
#         if dish in cook_book:
#             for consist in cook_book[dish]:
#                 if consist['product'] in result:
#                     result[consist['product']]['quantity'] += consist['quantity'] * person_count
#                 else:
#                     result[consist['product']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
#         else:
#             print('Такого блюда нет в книге')
#     print(result)
# get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])

with open("1.txt", encoding='utf-8') as f:
    data_1 = dict.fromkeys(['1.txt'],[])
    for row in f:
        data_1['1.txt'].append(row.strip())
with open('2.txt', encoding="UTF-8") as f:
    data_2 = dict.fromkeys(['2.txt'],[])
    for row in f:
        data_2['2.txt'].append(row.strip())
with open('3.txt', encoding='UTF-8') as f:
    data_3 = dict.fromkeys(['3.txt'],[])
    for row in f:
        data_3['3.txt'].append(row.strip())
def sort(data_1, data_2, data_3):
    data_sort = data_1 | data_2 | data_3
    return dict(sorted(data_sort.items(), key=lambda item: len(item[1])))
with open('4.txt','w', encoding='UTF-8') as f:
    for key, value in sort(data_1, data_2, data_3).items():
        f.write(f'{key}\n')
        f.write(f'{len(value)}\n')
        for row in value:
            f.write(f'{row}\n')



