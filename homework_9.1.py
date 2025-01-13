import re
def popular_words (text, words): 
	text = text.lower()
	word_counts = {}
	for word in words:
		count = len(re.findall(r'\b' + re.escape(word) + r'\b', text))
		word_counts[word] = count
	return word_counts
	
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1' 
print('OK')