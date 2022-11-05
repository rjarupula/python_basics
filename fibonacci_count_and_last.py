#method using function

def fibo(n):
  if n <= 1:
    return n
  else:
    return (fibo(n-1) + fibo(n-2))
  
  

#Get the number for Fibonacci series to find value
fib_num = int(input())
#Find the fibonacci value for the position of fib_num
if fib_num < 0:
  print("Please enter any Positive Number")
else:
  #Case 1 for Positional Value
  print(fibo(fib_num))
  #Case 2 for Series of values of Fibonacci
  for i in range(fib_num):
    print(fibo(i))
  #Case 3 For Sum of the all numbers in Fibonacci Series
  sum = 0
  for i in range(fib_num):
    sum += fibo(i)
print("Sum of all the Numbers in Fibonacci is : {}".format(sum))
