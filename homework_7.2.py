def correct_sentence(text):
	if len (text) > 0:
		if not text.endswith("."):
			text += "."

		if not text[0].isupper():
			text = text[0].upper() + text [1:]
	return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1' 
assert correct_sentence("hello") == "Hello.", 'Test2' 
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3' 
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4' 
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5' 
print('ОК')
