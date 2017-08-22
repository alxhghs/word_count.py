file_location = "/Users/Alex/Programming/Python/word counter/" + input("Enter file name: ")

"""read text and split into a list"""
with open (file_location, "r") as myfile:
    text = myfile.read().replace("\n", "")

text = text.split()

"""read don't count words and split into a list"""
with open ("dont_count.txt", "r") as myfile:
    dont_count_words = myfile.read().replace("\n", "")
    
dont_count_words = dont_count_words.split()

word_count = {}
initial_word_value = 0


"""lowers all the words in a list"""
def lower(list):
	return [word.lower() for word in list] # lowers the words in the dictionary


text = lower(text)
dont_count_words = lower(dont_count_words)


"""adds the word if it wasn't in the dictionary already"""
for word in text:
	if word not in dont_count_words:
		if word not in word_count:
			word_count[word] = initial_word_value


"""increases the key by 1 if in the dictionary already"""
for word in text:
	if word in word_count:
		word_count[word] += 1

"""Gets the max word length"""
max_length = 0
for word in text:
	if len(word) > max_length:
		max_length = len(word)

"""prints the values and adds spacing"""
for key, value in sorted(word_count.items()):
	spacing = max_length - len(key)
	x = ""
	for space in range(0, spacing):
		x += " "

	print(f'Key: {key} {x}| Value:{value}')
