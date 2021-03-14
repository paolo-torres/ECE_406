"""
ECE406, W'21, Assignment 3, Problem 1(c) 
Skeleton solution file.
"""

"""
You are not allowed to import anything. If we see any import
statement, you earn an automatic 0.
"""

"""
You need to implement this method.

You are certainly allowed to define any subroutines you want
above this method in this file.

We will test with inputs that match the spec only --- a string
str([[a,b], [c,d]]) is a valid key of c if and only if a move
[a,b] to [c,d] is valid. src is a valid source square, i.e.,
s[0] == 1. You should return a list, which is a path from the src
square to one of the destination squares that is the cheapest
from src to one of the destination squares.
"""

def robotpath(n, src, c):
    xSrc = src[0] - 1
    ySrc = src[1] - 1

    dp = [[float('inf') for i in range(n)] for j in range(n)]
    dp[xSrc][ySrc] = 1

    numMoves = len(c)
    moves = [[0 for i in range(numMoves)] for j in range(numMoves)]
    costs = [0 for i in range(numMoves)]

    i = 0
    for move in c:
        j = 0
        for index in move:
            if (index.isdigit()):
                moves[i][j] = int(index) - 1
                j = j + 1
        
        costs[i] = c[move]

        i = i + 1
        j = 0

    pos = []

    for i in range(len(moves)):
        xCurr = moves[i][0]
        yCurr = moves[i][1]
        xNext = moves[i][2]
        yNext = moves[i][3]

        cost = costs[i]

        if (dp[xCurr][yCurr] != float('inf')):
            print('Move:', xCurr, yCurr, '->', xNext, yNext, 'Cost:', cost)

        if (dp[xNext][yNext] > dp[xCurr][yCurr] + cost):
            if (dp[xNext][yNext] != float('inf')):
                for j in range(len(pos)):
                    if (pos[j][2] == xNext and pos[j][3] == yNext):
                        if (pos[j][4] > cost):
                            pos[j][0] = xCurr
                            pos[j][1] = yCurr
                            pos[j][4] = cost
            else:
                pos.append([xCurr, yCurr, xNext, yNext, cost])
            dp[xNext][yNext] = dp[xCurr][yCurr] + cost
    
    for i in range(n):
        print(dp[i])
    
    pos.reverse()

    xStart = pos[0][0]
    yStart = pos[0][1]
    xEnd = pos[0][2]
    yEnd = pos[0][3]
    cost = pos[0][4]

    for i in pos:
        if (xEnd == i[2] and cost > i[4]):
            xStart = i[0]
            yStart = i[1]
            xEnd = i[2]
            yEnd = i[3]
            cost = i[4]

    path = []

    for i in range(n):
        for j in pos:
            if (xEnd == j[2]):
                if (yEnd == j[3] and cost > j[4]):
                    xStart = j[0]
                    yStart = j[1]
                    xEnd = j[2]
                    yEnd = j[3]
                    cost = j[4]
        path.append([xEnd, yEnd])
        xEnd = xStart
        yEnd = yStart
        cost = float('inf')
    
    path.reverse()

    for i in range(len(path)):
        path[i][0] = path[i][0] + 1
        path[i][1] = path[i][1] + 1
    
    print(path)

    return path
