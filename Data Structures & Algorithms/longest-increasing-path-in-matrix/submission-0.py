class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ## DFS with memo
        ## memo is going to store the max path len starting each node

        rows, cols = len(matrix), len(matrix[0])

        memo = [[0 for _ in range(cols)]for _ in range(rows)]

        def DFS(curR, curC):

            if memo[curR][curC] > 0:
                return memo[curR][curC]
            
            result = 1
            
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                newR = curR + dr
                newC = curC + dc
                if 0 <= newR < rows and 0 <= newC < cols and matrix[curR][curC] < matrix[newR][newC]:
                    result = max(result, DFS(newR, newC) + 1)
            
            memo[curR][curC] = result
            
            return result

        self.ans = 1
        for r in range(rows):
            for c in range(cols):
                self.ans = max(self.ans, DFS(r, c))

        return self.ans