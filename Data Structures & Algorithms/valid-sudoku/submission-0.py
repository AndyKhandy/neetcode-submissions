class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                if(value in cols[j] or value in rows[i] or value in squares[(i // 3, j // 3)]):
                    return False
                
                cols[j].add(value)
                rows[i].add(value)
                squares[(i//3, j//3)].add(value)

        return True