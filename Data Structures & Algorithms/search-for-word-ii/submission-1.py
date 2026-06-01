class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        ## init trie
        for w in words:
            trie.insert(w)

        rows, cols = len(board), len(board[0])
        ans = set()
        dire = [(1,0), (-1,0), (0,1), (0,-1)]

        seen = set()

        def dfs(r, c, node):
            if node.word:
                ans.add(node.word)
            
            seen.add((r, c))
            for dr, dc in dire:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen:
                    if board[nr][nc] in node.child:
                        dfs(nr, nc, node.child[board[nr][nc]])
            seen.remove((r, c)) 

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie.root.child:
                    curNode = trie.root.child[board[r][c]]
                    dfs(r, c, curNode)
                    seen = set()
        return list(ans)










