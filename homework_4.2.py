lst = [0, 1, 7, 2, 4, 8]
if not lst:
	result =0

else:
	numbers_sum = 0
	for num in range(0, len(lst), 2):
		numbers_sum +=lst[num]
	result = numbers_sum*lst[-1]
print(result)