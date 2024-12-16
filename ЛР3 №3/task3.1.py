# TODO Напишите функцию для поиска индекса товара

def find_first_item(inventory, item):
    for i, product in enumerate(inventory):
        if product == item:
            return i
    return None

# Пример использования функции
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_item(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")