lst = [12, 3, 4, 10, 8]

if len(lst) >1:
	last_number = lst[-1:]
	lst.insert(0, last_number[0])
	lst.pop(-1)
print(lst)