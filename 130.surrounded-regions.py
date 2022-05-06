#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Phase 1: “Save” every O-region touching the border, changing 
        its cells to ‘S’.
        Phase 2: Change every ‘S’ on the board to ‘O’ and everything 
        else to ‘X’.
        """
        # if not any(board): return

        # m, n = len(board), len(board[0])
        # save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), 
        #                                         (k, 0), (k, n-1))]
        # while save:
        #     i, j = save.pop()
        #     if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
        #         board[i][j] = 'S'
        #         save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        # board[:] = [['XO'[c == 'S'] for c in row] for row in board]

        rows_num = len(board)
        if rows_num <= 0:
            return board
        cols_num = len(board[0])
        if cols_num <= 0:
            return board
            
        for col_idx in range(cols_num):
            self.dfs(board, 0, col_idx, rows_num, cols_num)
            self.dfs(board, rows_num-1, col_idx, rows_num, cols_num)
        
        for row_idx in range(rows_num):
            self.dfs(board, row_idx, 0, rows_num, cols_num)
            self.dfs(board, row_idx, cols_num-1, rows_num, cols_num)
        
        for row_idx in range(rows_num):
            for col_idx in range(cols_num):
                if board[row_idx][col_idx] == 'O': 
                    board[row_idx][col_idx] = 'X'
                elif board[row_idx][col_idx] == 'Q':
                    board[row_idx][col_idx] = 'O'      
        return board            
        
    def dfs(self, board, yy, xx, rows_num, cols_num):
        if yy < 0 or yy >= rows_num or xx < 0 or xx >= cols_num or board[yy][xx] != 'O':
            return
        board[yy][xx] = 'Q'        
        self.dfs(board, yy-1, xx, rows_num, cols_num)
        self.dfs(board, yy+1, xx, rows_num, cols_num)
        self.dfs(board, yy, xx-1, rows_num, cols_num)
        self.dfs(board, yy, xx+1, rows_num, cols_num)

