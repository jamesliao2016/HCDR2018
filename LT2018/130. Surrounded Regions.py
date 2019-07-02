class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        m,n = len(board),len(board[0])
        save = []
        for i in [0,m-1]:
            for j in [0,n-1]:
                save += [[i,val] for val in range(n)]
                save += [[val,j] for val in range(m)]
        while save:
            i,j = save.pop()
            if 0<=i<m and 0<=j<n and board[i][j]=='O':
                board[i][j] = 'S'
                save += [i,j+1],[i,j-1],[i-1,j],[i+1,j]
        board[:] = [ ['XO'[x=='S'] for x in row] for row in board]


if __name__ == '__main__':

    '''

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the 
board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to 
an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent 
cells connected horizontally or vertically.
    
    '''