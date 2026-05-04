class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def buildGrid(queen_cols, n):
            result = []
            for c in queen_cols:
                row = "." * c + "Q" + (n - c - 1) * "."
                result.append(row)
            return result

        ans = []
        queen_cols = []
        rows = set()
        cols = set()
        diag1 = set() ## row + col
        diag2 = set() ## row - col
           
        def helper (row):
            if row == n:
                ans.append(buildGrid(queen_cols, n))
            
            for c in range(n):
                if row in rows or c in cols or (row - c) in diag2 or (row + c) in diag1:
                    continue
                
                rows.add(row)
                cols.add(c)
                diag1.add(row + c)
                diag2.add(row - c)
                queen_cols.append(c)
                
                helper(row+1)

                rows.remove(row)
                cols.remove(c)
                diag1.remove(row+c)
                diag2.remove(row-c)
                queen_cols.pop()
        helper(0)
        return ans
        