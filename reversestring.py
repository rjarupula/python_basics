s = input()
r = ''
for i in range(1, len(s)+1):
	r += s[-i]
print(r)
