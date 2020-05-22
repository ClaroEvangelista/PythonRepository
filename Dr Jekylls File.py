# 6.1.9.17
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
# srcname = "C:\\Users\\owner\\PycharmProjects\\MyProj\\filedoesNOTexist.txt"
# srcname = "C:\\Users\\owner\\PycharmProjects\\MyProj\\empty.txt"
# srcname = "C:\\Users\\owner\\PycharmProjects\\MyProj\\badline.txt"
# srcname = "C:\\Users\\owner\\PycharmProjects\\MyProj\\notes.txt"
srcname = "C:/Users/owner/PycharmProjects/MyProj/notes.txt"
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
