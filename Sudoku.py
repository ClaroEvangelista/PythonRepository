"""
5.1.11.11
This my version of the Sudoku game
Choose between goodsudoku or badsudoku
Note: sudokupassorfail is used as the grand daddy of Pass or Fail
      white passorfail is used when checking horizontally, vertically and when checking the 9 3x3 cubes.
      Any single 'Fail' will fail the sudoku
"""


def validate():
    global sudokupassorfail
    passorfail = True

    # Validate Horizontally
    for x in range(9):
        No1Found = No2Found = No3Found = No4Found = No5Found = No6Found = No7Found = No8Found = No9Found = False
        for y in range(9):
            if lst[x][y] == '1': No1Found = True
            elif lst[x][y] == '2': No2Found = True
            elif lst[x][y] == '3': No3Found = True
            elif lst[x][y] == '4': No4Found = True
            elif lst[x][y] == '5': No5Found = True
            elif lst[x][y] == '6': No6Found = True
            elif lst[x][y] == '7': No7Found = True
            elif lst[x][y] == '8': No8Found = True
            elif lst[x][y] == '9': No9Found = True
        print('row:', x+1, '1:', No1Found, '2:', No2Found, '3:', No3Found, '4:', No4Found, '5:', No5Found, '6:', No6Found, '7:', No7Found, '8:', No8Found, '9:', No9Found)
        if No1Found == False or No2Found == False or No3Found == False or + \
                No4Found == False or No5Found == False or No6Found == False or + \
                No7Found == False or No8Found == False or No9Found == False:
            passorfail = False
            sudokupassorfail = False


    # Validate Vertically
    for x in range(9):
        No1Found = No2Found = No3Found = No4Found = No5Found = No6Found = No7Found = No8Found = No9Found = False
        for y in range(9):
            if lst[y][x] == '1': No1Found = True
            elif lst[y][x] == '2': No2Found = True
            elif lst[y][x] == '3': No3Found = True
            elif lst[y][x] == '4': No4Found = True
            elif lst[y][x] == '5': No5Found = True
            elif lst[y][x] == '6': No6Found = True
            elif lst[y][x] == '7': No7Found = True
            elif lst[y][x] == '8': No8Found = True
            elif lst[y][x] == '9': No9Found = True
        print('col:', x+1, '1:', No1Found, '2:', No2Found, '3:', No3Found, '4:', No4Found, '5:', No5Found, '6:', No6Found, '7:', No7Found, '8:', No8Found, '9:', No9Found)
        if No1Found == False or No2Found == False or No3Found == False or + \
                No4Found == False or No5Found == False or No6Found == False or + \
                No7Found == False or No8Found == False or No9Found == False:
            passorfail = False
            sudokupassorfail = False

    return passorfail


def validate3x3(a, b):
    global sudokupassorfail
    passorfail = True
    No1Found = No2Found = No3Found = No4Found = No5Found = No6Found = No7Found = No8Found = No9Found = False
    # Search Horizontally
    for x in range(a, a + 3):
        for y in range(b, b + 3):
            # print(x,y)
            print(lst[x][y], end='')
            if lst[x][y] == '1': No1Found = True
            elif lst[x][y] == '2': No2Found = True
            elif lst[x][y] == '3': No3Found = True
            elif lst[x][y] == '4': No4Found = True
            elif lst[x][y] == '5': No5Found = True
            elif lst[x][y] == '6': No6Found = True
            elif lst[x][y] == '7': No7Found = True
            elif lst[x][y] == '8': No8Found = True
            elif lst[x][y] == '9': No9Found = True

    print('\n', '1:', No1Found, '2:', No2Found, '3:', No3Found, '4:', No4Found, '5:', No5Found, '6:', No6Found, '7:', No7Found, '8:', No8Found, '9:', No9Found)
    if No1Found == False or No2Found == False or No3Found == False or + \
            No4Found == False or No5Found == False or No6Found == False or + \
            No7Found == False or No8Found == False or No9Found == False:
        passorfail = False
        sudokupassorfail = False

    return passorfail


# Also Bad
sudokufail = ("""
195743862
431865927
876192545
387459216
612387493
549216738
763524189
928671354
254938671""")

# Bad
# sudokufail = ("""
# 195743862
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 254938671""")

# Good
sudokupass = ("""
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672""")

sudokupassorfail = True

# Starts Here
x = input('Please select between "Sudoku Pass" or "Sudoku Fail", type p or f: ')

if x == 'p':
    lst = sudokupass.split()
else:
    lst = sudokufail.split()

#lst = input.split()

sudoku="+===+===+===+===+===+===+===+===+===+\n| " + lst[0][0] + " | " + lst[0][1] + " | " + lst[0][2] + " | " + lst[0][3] + " | " + lst[0][4] + " | " + lst[0][5] + " | " + lst[0][6] + " | " + lst[0][7] + " | " + lst[0][8] + " |\n" + \
       "+===+===+===+===+===+===+===+===+===+\n| " + lst[1][0] + " | " + lst[1][1] + " | " + lst[1][2] + " | " + lst[1][3] + " | " + lst[1][4] + " | " + lst[1][5] + " | " + lst[1][6] + " | " + lst[1][7] + " | " + lst[1][8] + " |\n" + \
       "+===+===+===+===+===+===+===+===+===+\n| " + lst[2][0] + " | " + lst[2][1] + " | " + lst[2][2] + " | " + lst[2][3] + " | " + lst[2][4] + " | " + lst[2][5] + " | " + lst[2][6] + " | " + lst[2][7] + " | " + lst[2][8] + " |\n" + \
       "+===+===+===+===+===+===+===+===+===+\n| " + lst[3][0] + " | " + lst[3][1] + " | " + lst[3][2] + " | " + lst[3][3] + " | " + lst[3][4] + " | " + lst[3][5] + " | " + lst[3][6] + " | " + lst[3][7] + " | " + lst[3][8] + " |\n" + \
       "+===+===+===+===+===+===+===+===+===+\n| " + lst[4][0] + " | " + lst[4][1] + " | " + lst[4][2] + " | " + lst[4][3] + " | " + lst[4][4] + " | " + lst[4][5] + " | " + lst[4][6] + " | " + lst[4][7] + " | " + lst[4][8] + " |\n" + \
       "+===+===+===+===+===+===+===+===+===+\n| " + lst[5][0] + " | " + lst[5][1] + " | " + lst[5][2] + " | " + lst[5][3] + " | " + lst[5][4] + " | " + lst[5][5] + " | " + lst[5][6] + " | " + lst[5][7] + " | " + lst[5][8] + " |\n" + \
       "+===+===+===+===+===+===+===+===+===+\n| " + lst[6][0] + " | " + lst[6][1] + " | " + lst[6][2] + " | " + lst[6][3] + " | " + lst[6][4] + " | " + lst[6][5] + " | " + lst[6][6] + " | " + lst[6][7] + " | " + lst[6][8] + " |\n" + \
       "+===+===+===+===+===+===+===+===+===+\n| " + lst[7][0] + " | " + lst[7][1] + " | " + lst[7][2] + " | " + lst[7][3] + " | " + lst[7][4] + " | " + lst[7][5] + " | " + lst[7][6] + " | " + lst[7][7] + " | " + lst[7][8] + " |\n" + \
       "+===+===+===+===+===+===+===+===+===+\n| " + lst[8][0] + " | " + lst[8][1] + " | " + lst[8][2] + " | " + lst[8][3] + " | " + lst[8][4] + " | " + lst[8][5] + " | " + lst[8][6] + " | " + lst[8][7] + " | " + lst[8][8] + " |\n" + \
       "+===+===+===+===+===+===+===+===+===+"
print(sudoku)

# Validate horizontally and then vertically
print('validate result (all good so far if True): ', validate(), '\n')

# Validate the 9 3x3 cubes
print('1st cube check (good if True):', validate3x3(0, 0), '\n')
print('2nd cube check (good if True):', validate3x3(0, 3), '\n')
print('3rd cube check (good if True):', validate3x3(0, 6), '\n')

print('4th cube check (good if True):', validate3x3(3, 0), '\n')
print('5th cube check (good if True):', validate3x3(3, 3), '\n')
print('6th cube check (good if True):', validate3x3(3, 6), '\n')

print('7th cube check (good if True):', validate3x3(6, 0), '\n')
print('8th cube check (good if True):', validate3x3(6, 3), '\n')
print('9th cube check (good if True):', validate3x3(6, 6), '\n')

if sudokupassorfail:
    print('Sudoku PASSED')
else:
    print('Sudoku FAILED')