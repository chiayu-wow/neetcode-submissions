class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set()
        dire = [(1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,-1,0,0), (0,0,1,0),(0,0,-1,0), (0,0,0,1),(0,0,0,-1)]

        dead = set(deadends)
        qu = deque()
        seen.add("0000")
        qu.append([0,0,0,0])
        
        ans = 0
        while qu:
            size = len(qu)
            for _ in range(size):
                cur = qu.popleft()

                if "".join(str(x) for x in cur) in dead:
                    continue
                
                if "".join(str(x) for x in cur) == target:
                    return ans
                
                for d1, d2, d3, d4 in dire:
                    newPos = [cur[0] + d1, cur[1] + d2, cur[2] + d3, cur[3] + d4]

                    for n in range(4):
                        newPos[n] = newPos[n] + 10 if newPos[n] < 0 else newPos[n]
                        newPos[n] = newPos[n] % 10 if newPos[n] >= 10 else newPos[n]
                   
                    newStr = "".join(str(x) for x in newPos)
                    ## print(curStr)
                    if newStr not in seen and newStr not in dead:
                        qu.append(newPos)
                        seen.add(newStr)
            ans += 1
        
        return -1
