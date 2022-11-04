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
	
