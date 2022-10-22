list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
List_with_index = list(enumerate(list_numbers,0))
max_ = max (List_with_index, key=lambda i: i[1])
max_index = max_[0]
max_value = max_[1]
last_number = list_numbers[-1]

list_numbers[-1] = max_value

list_numbers[max_index] = last_number

print(list_numbers)