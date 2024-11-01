# TODO Напишите функцию find_common_participants
def find_common_participants(first_group: str, second_group: str, separator: str = ','):
    return sorted(set(first_group.split(separator)) & set(second_group.split(separator)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, separator='|'))
print(find_common_participants(participants_first_group, participants_second_group))