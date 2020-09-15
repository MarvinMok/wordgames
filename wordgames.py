points = {

	"a": 1,
	"b": 3,
	"c": 3,
	"d": 2,
	"e": 1, 
	"f": 4,
	"g": 2,
	"h": 4,
	"i": 1,
	"j": 8,
	"k": 5,
	"l": 1,
	"m": 3,
	"n": 1,
	"o": 1,
	"p": 3,
	"q": 10,
	"r": 1,
	"s": 1,
	"t": 1,
	"u": 1,
	"v": 4,
	"w": 4,
	"x": 8,
	"y": 4,
	"z": 10, 
}




def main():
	with open("names.txt", 'r') as f:
		for line in f:
			print(line)


def get_points(s):
	sum = 0;
	for i in range(0, len(s)):
		sum = sum + points[s[i].lower()]
	return sum

def isValidWord(s, words):
	valid = []
	length = len(s)
	wordsWithLength = words[length]
	for i in range(0, len(wordsWithLength)):
		if (sorted(s) == sorted(wordsWithLength[i])):
			valid.append(wordsWithLength[i])
	
	return valid 



def defineWords():
	words = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[]} 
	with open("words.txt", 'r') as f:
		for line in f:
			linelength = len(line) - 1
			words[linelength].append(line[0:linelength])
	return words

if __name__ == '__main__':
	value = get_points("maz")
	print (value)


	words = defineWords()

	print (isValidWord("AA", words))

"""
1) find value of word
2) given 7 letters, check if it can be formed into a scrabble word
3) 
"""