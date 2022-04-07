TheBoard = {'top-L': ' ', 'top-R': ' ', 'top-M': ' ',
'mid-L': ' ', 'mid-R': ' ', 'mid-M': ' ',
'low-L': ' ', 'low-R': ' ', 'low-M': ' ',}

def PrintBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('------')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

PrintBoard(TheBoard)
