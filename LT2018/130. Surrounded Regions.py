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
        # save = [['X']*n for _ in range(m)]
        for i in [0,m-1]:
            for j in [0,n-1]:
                tmp1 = [[i,k] for k in range(n)]
                tmp2 = [[k,j] for k in range(m)]
                save += tmp1
                save += tmp2
        while save:
            i,j = save.pop()
            if 0<=i<m and 0<=j<n and board[i][j] == 'O':
                board[i][j] = 'X'
                save += [i,j-1],[i,j+1],[i-1,j],[i+1,j]
        # board[:] = [['XO'[x == 'O'] for x in row] for row in board]
        return board






if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    res = Solution().solve(board)
    print(res)

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

# 1 MAR, 2020
        if not any(board):
            return
        len_x,len_y = len(board), len(board[0])
        tmp_save = []
        for val_x in [0, len_x-1]:
            for val_y in [0,len_y-1]:
                tmp_save += [[val_x,tmp_j] for tmp_j in range(len_y)]
                tmp_save += [[tmp_i,val_y] for tmp_i in range(len_x)]
                
        while tmp_save:
            tmp_i,tmp_j = tmp_save.pop()
            if 0<=tmp_i<len_x and 0<=tmp_j<len_y and board[tmp_i][tmp_j] == "O":
                board[tmp_i][tmp_j] = "S"
                tmp_save += [tmp_i,tmp_j-1], [tmp_i,tmp_j+1],[tmp_i-1,tmp_j],[tmp_i+1,tmp_j]
        
        board[:] = [["XO"[val_x=="S"] for val_x in val_y] for val_y in board]

# 9 july 2019
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
                save += [i,j+1],[i,j-1],[i+1,j],[i-1,j]
        board[:] = [['XO'[val=='S'] for val in row] for row in board]
        return board


# 3 july, 2019
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
    
    '''