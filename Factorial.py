#Method 1
def factorial(n):
  if n == 1 or n == 0:
    return n
  else:
    return n * factorial(n-1)

  
#Function Call
#Get number for Factorial from User
num = int(input())
if num < 0:
  print("Please enter a Positve Number")
else:
  print("Factorial of {} is {}".format(num, factorial(num)))
  
  
