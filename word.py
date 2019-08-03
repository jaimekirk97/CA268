def get_plural(word):
	if word[-2:] == "ch" or "sh":
		word = word + "es"
	elif word[-1] == "x" or "s" or "z" or "o":
		word = word + "es"
	elif word[-2:] == "fe":
		word = word[:-2] + "ves"
	elif word[-1] == "f":
		word = word[:-1] + "ves"
	elif word[-1] == "y":
		word = word[:-1] + "ies"
	else:
		word = word + "s"
	return word

