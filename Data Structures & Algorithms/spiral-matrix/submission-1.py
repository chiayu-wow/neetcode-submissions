class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dire = [(0,1), (1,0), (0,-1), (-1,0)]
        rows, cols = len(matrix), len(matrix[0])
        seen = set() 
        ans = []

        def DFS(row, col, d):
            ans.append(matrix[row][col])

            change = 0

            while change < 4:
                dr, dc = dire[(d + change)%4]

                newR = row + dr
                newC = col + dc

                if 0 <= newR < rows and 0 <= newC < cols and (newR, newC) not in seen:
                    seen.add((newR, newC))
                    DFS(newR, newC, (d + change)%4)
                    break
                
                change += 1

        seen.add((0,0))
        DFS(0,0,0)
        return ans