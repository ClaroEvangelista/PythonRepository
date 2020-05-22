"""
4.1.6.13 PROJECT: Tic-Tac-Toe
This is my version of the Tic-Tac-Toe game
You will move first and your moves will show as 'o' while the computer show as 'x'
"""

from random import shuffle
# from IPython.display import clear_output   < this works in Jypyther Notebook only


def updatechessboard(input, x_OR_o):
    global no1 ,no2, no3, no4, no5, no6, no7, no8, no9
    if input == '1': no1 = x_OR_o
    if input == '2': no2 = x_OR_o
    if input == '3': no3 = x_OR_o
    if input == '4': no4 = x_OR_o
    if input == '5': no5 = x_OR_o
    if input == '6': no6 = x_OR_o
    if input == '7': no7 = x_OR_o
    if input == '8': no8 = x_OR_o
    if input == '9': no9 = x_OR_o
    chessboard = "+===+===+===+\n| " + no1 + " | " + no2 + " | " + no3 + " |\n" + \
                 "+===+===+===+\n| " + no4 + " | " + no5 + " | " + no6 + " |\n" + \
                 "+===+===+===+\n| " + no7 + " | " + no8 + " | " + no9 + " |\n" + \
                 "+===+===+===+"
    return chessboard


def checkiftheresawin(x_OR_o):
    global no1, no2, no3, no4, no5, no6, no7, no8, no9
    if ((no1 == x_OR_o and no2 == x_OR_o and no3 == x_OR_o) or
        (no4 == x_OR_o and no5 == x_OR_o and no6 == x_OR_o) or
        (no7 == x_OR_o and no8 == x_OR_o and no9 == x_OR_o) or
        (no1 == x_OR_o and no4 == x_OR_o and no7 == x_OR_o) or
        (no2 == x_OR_o and no5 == x_OR_o and no8 == x_OR_o) or
        (no3 == x_OR_o and no6 == x_OR_o and no9 == x_OR_o) or
        (no1 == x_OR_o and no5 == x_OR_o and no9 == x_OR_o) or
        (no3 == x_OR_o and no5 == x_OR_o and no7 == x_OR_o)):
        if x_OR_o == 'o':
            return 'You won!'
        else:
            return 'The computer won!'


def updateavailable(y):
    templist = []
    for x in available:
        if x != y: templist.append(x)
    return templist


def resetchessboard():
    global available, no1 ,no2, no3, no4, no5, no6, no7, no8, no9
    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    no1 = '1'
    no2 = '2'
    no3 = '3'
    no4 = '4'
    no5 = '5'
    no6 = '6'
    no7 = '7'
    no8 = '8'
    no9 = '9'
    chessboard = "+===+===+===+\n| " + no1 + " | " + no2 + " | " + no3 + " |\n" + \
                 "+===+===+===+\n| " + no4 + " | " + no5 + " | " + no6 + " |\n" + \
                 "+===+===+===+\n| " + no7 + " | " + no8 + " | " + no9 + " |\n" + \
                 "+===+===+===+"
    return chessboard


# tempint = 0
# templist = []

# global variables within the functions
available = []
no1 = no2 = no3 = no4 = no5 = no6 = no7 = no8 = no9 = ''

print(resetchessboard())

while True:
    inputo = input('Please select one of these numbers: ' + str(available) + '  ')

    if inputo not in str(available):
        print('Your input', inputo, 'is not valid. Please try again.')
    else:
        # clear_output()                   # << clears the prints, works in Jupyter notebook only
        print(updatechessboard(inputo, 'o'))

        win = checkiftheresawin('o')
        if win != None:
            print(win + ' The End!')
            YesOrNo = input("Want to play again? Type a y: ")
            if YesOrNo == 'y':
                print(resetchessboard())
                continue
            else:
                break

        available = updateavailable(int(inputo))
        if len(available) == 0:
            print('It\'s a draw. THE END!!!')
            YesOrNo = input("Want to play again? Type a y: ")
            if YesOrNo == 'y':
                print(resetchessboard())
                continue
            else:
                break

        templist = available[:]  # the [:] is to insure that available will not be affected by the shuffle
                                 # the [:] will create two different list.
        shuffle(templist)        # makes the computer move pseudo random, check the import above
        tempint = templist[0]
        print('Computer picked: ', tempint)

        print(updatechessboard(str(tempint), 'x'))

        win = checkiftheresawin('x')
        if win != None:
            print(win + ' The End!')
            YesOrNo = input("Want to play again? Type a y: ")
            if YesOrNo == 'y':
                print(resetchessboard())
                continue
            else:
                break

        available = updateavailable(tempint)