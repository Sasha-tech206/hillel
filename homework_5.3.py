import string

text = input("Введіть текст: ")

hashtag = "#"
word_started = False
for char in text:
    if char not in string.punctuation:
        if not word_started:
            hashtag += char.upper()
            word_started = True
        elif char == " ":
            word_started = False
        else:
            hashtag += char.lower()

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)