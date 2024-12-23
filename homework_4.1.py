lst = [1, 12, 0, 0, 0, 5]

result = []

for num in lst:
	if num != 0:
		result.append(num)

for num in lst:
	if num == 0:
		result.append(num)

print(result)