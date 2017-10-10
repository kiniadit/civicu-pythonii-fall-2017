import re
def is_isogram(string):
	#replace all punctuations (incl. '_') with '' and convert to lower case
	string = re.sub('[_\W]+','',string.lower())
	#convert to a set to remove duplicates and check if length remains the same
	return len(set(string)) == len(string)
    

