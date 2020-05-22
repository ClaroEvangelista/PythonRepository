"""
6.1.9.17
Originally this was designed to take an input() but I got tired of copying and pasting so I hard-coded
We were instructed to create new exceptions and to test them out
Just uncomment the scrname lines below to test for different scenarios

Notes.txt:             <<< this is the good input, it has fname, lname and score, 3 elements
John Smith 5
Anna Boleyn 4.5
John Smith 2           <<< dupe #1 will be merged into 1 line and John's score will 5 + 2 = 7
Anna Boleyn 11         <<< dupe #2 wiil be merged into 1 line and Anna's score will 4.5 + 11 = 15.5
Andrew Cox 1.5

badline.txt:           <<< used for badline exception testing
John Smith 5
Anna Boleyn 4.5
one two three four     <<< this will cause a badline exception

Output (sorted by dict key):
Andrew Cox 1.5
Anna Boleyn 15.5
John Smith 7.0
"""

from os import strerror

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self, message)

class FileEmpty(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self, message)

inputx = ''
dic = {}
fullname = ''
# srcname = input("Please select Prof. Jekyll's file: ")  # C:\Users\owner\PycharmProjects\MyProj\notes.txt
# srcname = "C:\\Users\\owner\\PycharmProjects\\MyProj\\filedoesNOTexist.txt"  # will cause IOError exception
# srcname = "C:\\Users\\owner\\PycharmProjects\\MyProj\\empty.txt"             # will cause FileEmpty exception
# srcname = "C:\\Users\\owner\\PycharmProjects\\MyProj\\badline.txt"           # will cause BadLine exception
# srcname = "C:\\Users\\owner\\PycharmProjects\\MyProj\\notes.txt"             # good file: double \ windows style
srcname = "C:/Users/owner/PycharmProjects/MyProj/notes.txt"                    # also good: single / linux style
# Note: Python uses the \ as an escape character (like \n) # 6.1.8.3
try:
    src = open(srcname, "rt")
    inputx = src.readlines()    # returns a list of strings, each string is a line of text 6.1.9.5
    src.close()
    if len(inputx) == 0:
        raise FileEmpty("Error: The file you selected is empty")
    for x in range(len(inputx)):
        temp = inputx[x].split()
        if len(temp) != 3:
            raise BadLine("Error: BadLine on the input file on line: " + str(x + 1))
        fullname = temp[0] + ' ' + temp[1]
        if fullname not in dic:
            dic[fullname] = float(temp[2])
        else:
            dic[fullname] += float(temp[2])
except FileEmpty as fe:
    print(fe)
    exit(1)
except BadLine as bl:
    print(bl)
    exit(2)
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)

print('\n')
for key in sorted(dic.keys()):
    print(key, dic[key])

# the method below doesn't work: AttributeError: 'dict_keys' object has no attribute 'sort'
# for key in (dic.keys()).sort:
#     print(key, dic[key])
