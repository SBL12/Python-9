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





#A list is an ordered collection of elements.
# List is a collection which is ordered and changeable.
# Allows duplicate members.
# These elements can be any type of data.



print("Welcome to python programing!")
print("Today  we will be learning  list data structure in deatails")
numbers = [12,100,0,1,5,23,25,26,101-1]
print("Original List of Numbers",numbers)

print(str(max(list)))

print(str(min(list)))

list.extend([100,200,300,400])
print(list)

list.append(200)

print(list)

list.sort()