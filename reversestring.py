#Basic method 1
s = input()
r = ''
for i in range(1, len(s)+1):
	r += s[-i]
print(r)

#Method 2 of Function based
def reverse(string):
	string = string[::-1]
	return string

#Method 3 of Function based with looping process
def reverseTwo(string):
	str = ""
	for i in string:
		str = i+str
	return str


#Taking input from User
string = input()

#Calling functions
#Method 2 function calling
print(reverse(string))

#Method 3 function calling
print(reverseTwo(string))
