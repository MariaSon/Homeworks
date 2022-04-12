import os


base_path = os.getcwd()
cook_dir = 'cook_book'
file_name = 'cook_recipes.txt'
full_path = os.path.join(base_path, cook_dir, file_name)


def recipe_book(name, encoding='utf-8'):
    cook_list = []
    cook_line = []
    with open(name, encoding=encoding) as file:
        recipe_lines = file.readlines()
        last_recipe_line = recipe_lines[-1]
        cook_book_dict = {}
        cooks = []
        cook_first = ''
        for element in recipe_lines:
            if element.strip() == '':
                cook_list.append(cook_line)
                cook_line = []
            elif element.strip() == last_recipe_line:
                cook_line.append(element.strip())
                cook_list.append(cook_line)
                cook_line = []
            else:
                cook_line.append(element.strip())
        for elements in cook_list:
            i = 0
            for element in elements:
                if i == 0:
                    cook_book_dict.setdefault(element)
                    cook_first = element
                    i += 1
                else:
                    if i == 1:
                        i += 1
                    else:
                        words = element.rstrip().split('|')
                        dict_keys = ['ingredient_name', 'quantity', 'measure']
                        dict_string = dict(zip(dict_keys, words))
                        cooks.append(dict_string)
            cook_book_dict[cook_first] = cooks
            cooks = []
    return cook_book_dict


cook_book = (recipe_book(full_path))


def get_shop_list_by_dishes(dishes_list, person_count):
    ingredients = {}
    for dish in dishes_list:
        if dish in cook_book.keys():
            for element in cook_book[dish]:
                ing_name = element['ingredient_name']
                element.pop('ingredient_name')
                element.values()
                element['quantity'] = int(element['quantity']) * person_count
                ing_prod = dict(sorted(element.items()))
                ingredients[ing_name] = ing_prod
        else:
            print(f'Блюдо - {dish} отсутствует в кулинарной книге!')
    return ingredients


print(get_shop_list_by_dishes(['Фахитос', 'Запеченный картофель'], 10))
