"""
6.1.9.16 - count characters and sort the dictionary using lambda
Maps and Lambdas
Original designed to take an input() but got tired of cutting and pasting
"""


from os import strerror

# srcname = input("Please select the source file: ")   # "C:\Users\owner\PycharmProjects\MyProj\input.txt"
# srcname = "C:\\Users\\owner\\PycharmProjects\\MyProj\\input.txt"  # this works
srcname = "C:/Users/owner/PycharmProjects/MyProj/input.txt"         # this works too with just one /
# Note: when hardcoding, must use double \\ otherwise if input() function is used, just use one \
# Note: Python uses the \ as an escape character (like \n) # 6.1.8.3
try:
    src = open(srcname, "rt")
    inputx = src.read().lower()    # read the whole file to the memory at once 6.1.9.3
    print(inputx)
    src.close()
    dst = open('C:\\Users\\owner\\PycharmProjects\\MyProj\\input.hist', 'wt')
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)

dic = {}
first = [0, 0]
second = [0, 0]
third = [0, 0]
for x in inputx:
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1

print(dic)

for key, value in dic.items():
    if value > first[1]:
        third[0] = second[0]
        third[1] = second[1]
        second[0] = first[0]
        second[1] = first[1]
        first[0] = key
        first[1] = value
    elif value > second[1]:
        third[0] = second[0]
        third[1] = second[1]
        second[0] = key
        second[1] = value
    elif value > third[1]:
        third[0] = key
        third[1] = value

print('First:  ', first)
print('Second: ', second)
print('Third:  ', third)

tempdic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}  # sorts on value - reversed
#tempdic = sorted(dic.items(), key=lambda item: item[1], reverse=True)  # creates a list with tuples(k:v) pair
print(tempdic)
#dic.clear()
dic = tempdic   # dic is tempdic = True

# write inputx to dst out file
# for x in inputx:
#     dst.write(x)
dst.write(inputx)
dst.write('\n')

for item in dic.items():
    if item[0] == '\n':
        dst.write('space')
    else:
        dst.write(item[0])
    dst.write(':')
    dst.write(str(item[1]))
    dst.write('\n')

dst.close()