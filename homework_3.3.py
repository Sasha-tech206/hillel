lst = [1, 2, 3, 4, 5]

if len(lst) == 0:
	result = [[], []]
	print(result)
else:
	mid = (len(lst) + 1) // 2
	first_part = lst[:mid]
	second_part = lst[mid:]
	result = [first_part, second_part]
	print(result)