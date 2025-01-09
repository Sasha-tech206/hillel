import random
def common_elements():
	set_of_threes = set(range(0, 101, 3))
	set_of_fives = set(range(0, 101, 5))
	common_elements = set_of_threes.intersection(set_of_fives)
	return common_elements

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Ok")