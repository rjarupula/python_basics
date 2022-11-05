def pown(a,n):
  if n <= 1:
    return a
  else:
    return a * pown(a, n-1)
  
#Get the numbers to Calculate the Power of a number
a, n = list(map(int, input().split(' ')))
if n < 0:
  print("Please enter a Positive number for Square")
  break
elif n == 0:
  print("the Power of {} ^ {} is :{}".format(a,n,1))
else:
  print("The Power of {} ^ {} is : {}".format(a, n, pown(a,n)))
