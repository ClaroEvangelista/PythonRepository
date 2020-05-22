# map takes a functions and an iterable

my_nums = [1, 2, 3, 4, 5]

# map example 1
def square(num):
    return num ** 2

# using a for-loop
for x in my_nums:
    print(square(x), end=' ')  # prints 1 4 9 16 26
print()


# displays a memory address of the map
map(square, my_nums)

# using a map in a for loop, same results
for x in map(square, my_nums):
    print(x, end=' ')  # prints 1 4 9 16 26
print()

# if you want a list
list(map(square, my_nums))  # creates a list [1, 4, 9, 16, 25]


# map example 2
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']
for x in map(splicer, names):
    print(x, end=' ')  # prints EVEN E S

# if you want a list
list(map(splicer, names))  # creates a list ['EVEN', 'E', 'S']
print()

# **NOTE** - when calling the square and splicer function,
# DO NOT call them with parenthesis (i.e. square() or splicer())
# because # 1 it will cause a type error and #2 the map will be calling them


# filter takes in a function and an iterable
def check_even(num):
    return num % 2 == 0

mynum = [1,2,3,4,5,6]

# creates a list of even numbers 2, 4, 6
print(list(filter(check_even, mynum)))   # creates and prints a list [2,4,6]

# using a for-loop with a filter
for x in filter(check_even, mynum):
    print(x, end=' ')                   # print 2 4 6
print()


# start of lambda
# start of lambda
# start of lambda

# lambda - anonymous function

#regular function
def square(num):
    return num ** 2
square(3)

#converted to lambda expression and assigned to square
square = lambda num: num ** 2
square(3)  # returns 9


#lamda and map together
my_nums =[1,2,3,4,5]

# map before conversion
def square(num):
    return num**2

# using a for-loop
for x in my_nums:
    print(square(x), end=' ')     # prints 1 4 9 16 25
print()

# converted to a lambda with map, all in 1 line
list(map(lambda num: num ** 2, my_nums))   # returns a list [1, 4, 9, 16, 25]
print(list(map(lambda num: num ** 2, my_nums))) # prints a list [1,4,9,16,25]


#converted to for-loop with a map and lambda expression
for x in map(lambda num: num ** 2, my_nums):   # prints 1, 4, 9, 16, 25
    print(x, end=' ')
print()

#lamda and filter together
my_nums =[1,2,3,4,5,6]

# before conversion
def check_even(num):
    return num % 2 == 0

# using a for-loop with a filter
for x in filter(check_even, mynum):
    print(x, end=' ')                  # prints 2 4 6

print()

# converted to a lambda with filter, all in 1 line
list(filter(lambda num: num % 2 == 0, my_nums)) # returns a list [2,4,6]
print(list(filter(lambda num: num % 2 == 0, my_nums))) # prints a list [2,4,6])


# converted to for-loop with a filter and lambda expression
for x in filter(lambda num: num % 2 == 0, my_nums):   # prints 2 4 6
    print(x, end=' ')
print()


# Another example of using map and lamdba together
names = ['Andy', 'Eve', 'Sally']
print(list(map(lambda x: x[0], names)))    # prints ['A', 'E', 'S']