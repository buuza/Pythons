#get list of distinct numbers
def distinct_num(numbers):
	res = []
	checked = []
	for x in numbers:
		if x not in checked:
			checked.append(x)
		else:
			res.append(x)
	return set(res)


print distinct_num([1, 1, 2, 3, 3, 3, 6, 7, 7])
print distinct_num([2, 2, 2, 1, 4, 3, 4, 4, 7])

#replace any character from given string
def char_replace(string, chars):
	found = string.find(chars)

	if found >= 0:
		return string[:found] + string[(found+len(chars)):]
	else:
		return 'CharacterNotFound'


print char_replace('soccer','c')