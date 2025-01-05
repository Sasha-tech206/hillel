import string

alphabet = string.ascii_letters

user_input = input("Enter two letters separated by '-': ")

dash_index = user_input.find('-')

start = user_input[:dash_index]
end = user_input[dash_index + 1:]

start_index = alphabet.index(start)
end_index = alphabet.index(end) + 1

result = alphabet[start_index:end_index]

print(result)