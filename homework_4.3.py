import random

lst = []

for i in range(random.randint(3, 10)):
	lst.append(random.randint(3, 10))

print(lst)
result = [lst[0], lst[2], lst[-2]]
print(result)