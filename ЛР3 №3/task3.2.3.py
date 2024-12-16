# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(group1, group2, delimiter=','):
    group1_set = set(group1.split(delimiter))
    group2_set = set(group2.split(delimiter))

    common_participants = group1_set.intersection(group2_set)
    return sorted(common_participants)

group1 = "Иванов,Петров,Сидоров"
group2 = "Петров,Васильев,Сидоров"

common_participants = find_common_participants(group1, group2)

print(f"Общие участники: {','.join(common_participants)}")

# TODO Провеьте работу функции с разделителем отличным от запятой

group1 = "Иванов|Петров|Сидоров"
group2 = "Петров|Васильев|Сидоров"

common_participants = find_common_participants(group1, group2, delimiter="|")

print(f"Общие участники: {','.join(common_participants)}")