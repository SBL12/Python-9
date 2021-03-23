## Write a program to generate a fibonaccui series of 
# write Fibonacci series up to n
#  """Print a Fibonacci series up to n.""

def fibonaci(n):
  a= 1
  b=1
  while (a< n):
    print(a)
    c = a+b
    a = b
    b = c

fibonaci(100)