numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index_of_none = numbers.index(None)
summ = sum(numbers[:index_of_none]+numbers[index_of_none+1:])
amount = len(numbers)
numbers[index_of_none] = summ/amount
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
