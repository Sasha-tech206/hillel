import re

def first_word(text):
    match = re.search(r"[a-zA-Z']+", text)
    if match:
        return match.group(0)
    return ""

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
assert first_word("") == "", 'Test7'
assert first_word("   ,.") == "", 'Test8'
assert first_word("123abc") == "abc", 'Test9'
assert first_word("'word") == "'word", 'Test10' 
print('OK')