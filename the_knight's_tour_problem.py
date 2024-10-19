'''
Given a N*N board with the Knight placed on the first block of an empty board. Moving according to the rules of chess knight must 
visit each square exactly once. Print the order of each cell in which they are visited.

Example:

Input : 
N = 8
Output:
0  59  38  33  30  17   8  63
37  34  31  60   9  62  29  16
58   1  36  39  32  27  18   7
35  48  41  26  61  10  15  28
42  57   2  49  40  23   6  19
47  50  45  54  25  20  11  14
56  43  52   3  22  13  24   5
51  46  55  44  53   4  21  12
'''



def isSafe(x,y,board):
    #utility function to check if the current position was visited or not
    if(x>=0 and y>=0 and x < n and y < n and board[x][y]==-1):
        return True #if the cell is not visited
    else:
        return False #vice-verse

def printSolution(n,board):
    #function to print the solution
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def solveKT(n):
    #function to solve the knight tour problem using backtracking and recursion
    #creating the board as per the user input
    board = [[-1 for i in range(n)] for i in range(n)]
    move_x = [2, 2, 1, -1, 1, -1, -2, -2] #possible moves along x-axis
    move_y = [1, -1, 2, 2, -2, -2, -1, 1] #possible moves along y-axis

    board[0][0]= 0 #since the knight is currently at the starting point (0,0)
    pos = 1 #position counter of the knight
    
    if(not solveKTutil(n,board,0,0,move_x,move_y,pos)):
        print("Solution not found")
        printSolution(n,board)
    else:
        #printing the solution in the board, if it exists
        printSolution(n,board)


def solveKTutil(n,board,cur_x,cur_y,move_x, move_y,pos):
    #if a solution exists return True
    if pos == n**2:
        return True
    
    for i in range(8): # running the loop from 0 to 8, to try all the possible combination of moves
        new_x = cur_x + move_x[i] #x position of the knight in the board, if it happens to be a valid position
        new_y = cur_y + move_y[i] #y position of the knight in the board, if it happens to be a valid position
        
        #to check if the current is move is valid or not
        if isSafe(new_x,new_y,board):
            #if the move is valid, update the board
            board[new_x][new_y]=pos
            #calling the function again to make a new move
            if solveKTutil(n,board,new_x,new_y,move_x,move_y,pos+1):
                return True
            #backtracking
            board[new_x][new_y]=-1
    #if there are no valid solution
    return False
    

#driver function
if __name__ == "__main__":
    #taking input from user
    n = int(input("Enter a number"))
    #calling the function to solve the problem
    solveKT(n)
