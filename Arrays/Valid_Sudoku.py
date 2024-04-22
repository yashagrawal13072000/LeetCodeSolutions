# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        result = []
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele != ".":
                    result += [(i, ele), (ele,j), (i // 3, j // 3, ele)]
        return len(result) == len(set(result))