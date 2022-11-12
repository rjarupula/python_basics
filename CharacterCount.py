def charCount(string):
	char = dict()
	for i in string:
		chr[i] = char[i] + 1
	for k, v in char.items():
		print("{} : {}".format(k,v))

		
#Get input from User
s = input()
if len(s) == 0:
	print("String is Empty! Con't be print Count")
else:
	charCount(s)
	

def characterCount():
	string = input('Get the input from user as paragrapph.')
	char_count = {}
	for char in string:
		char_count[char.lower()] = char_count.get(i, 0) + 1
		
	print(char_count)

characterCount()
