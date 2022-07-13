from pprint import pprint


def reader():
    with open('recipes.txt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            line = line.strip()
            cook_book.update({line: []})
            for ing in range(int(f.readline().strip())):
                lst = f.readline().strip().split('|')
                dictinary = {'ingredient_name': lst[0], 'quant': lst[1], 'measure': lst[2]}
                cook_book[line].append(dictinary)
            f.readline()

        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    products_list = {}
    for dish in dishes:
        for item in reader()[dish]:
            items_list = dict(
                [(item['ingredient_name'], {'measure': item['measure'], 'quant': int(item['quant']) * person_count})])
            if products_list.get(item['ingredient_name']):
                extra_item = (int(products_list[item['ingredient_name']]['quant']) +
                              int(items_list[item['ingredient_name']]['quant']))
                products_list[item['ingredient_name']]['quant'] = extra_item

            else:
                products_list.update(items_list)
    return products_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))