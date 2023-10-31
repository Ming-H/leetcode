#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        1. Iterate through the border cells of the matrix. If a border cell contains 'O', perform a DFS from that cell to mark all connected 'O' cells as visited.
        2. After the DFS, all the 'O' cells that are not visited are the ones that are surrounded by 'X'. Change those cells to 'X'.
        3. Iterate through the entire matrix and change all the visited cells back to 'O'.
        time complexity of the provided solution is O(m n)
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'V'  # Mark the cell as visited
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Step 1: DFS from border cells
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        # Step 2: Change surrounded 'O' cells to 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'

        return board
        