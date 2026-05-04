class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            rows = [set() for _ in range(9)]
            cols = [set() for _ in range(9)]
            box = [set() for _ in range(9)]

            for r in range(9):
                for c in range(9):
                    cur = board[r][c]

                    if cur == ".":
                        continue
                    
                    boxID = ((r//3) * 3) +  c // 3

                    if cur in cols[c] or cur in rows[r] or cur in box[boxID]:
                        return False
                    
                    cols[c].add(cur)
                    rows[r].add(cur)
                    box[boxID].add(cur)
            return True
        