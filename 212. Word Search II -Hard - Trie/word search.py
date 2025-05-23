from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}        # Dictionary to store child nodes keyed by characters
        self.isWord = False       # Flag to indicate if the node marks the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()    # Root node of the Trie

    def insert(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True         # Mark the end of a word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)       # Build the Trie from the list of words

        result = set()              # Use a set to avoid duplicate results

        def dfs(trieNode, r, c, current_word):
            # Check boundary conditions and whether current cell character exists in Trie children
            if (r < 0 or c < 0 or 
                r >= len(board) or c >= len(board[0]) or 
                board[r][c] not in trieNode.children):
                return

            temp = board[r][c]      # Current character
            board[r][c] = '#'       # Mark current cell as visited
            trieNode = trieNode.children[temp]
            current_word += temp    # Append current character to current word path

            if trieNode.isWord:     # If current path is a word in Trie, add to result set
                result.add(current_word)

            # Explore all 4 adjacent directions
            dfs(trieNode, r + 1, c, current_word)
            dfs(trieNode, r - 1, c, current_word)
            dfs(trieNode, r, c + 1, current_word)
            dfs(trieNode, r, c - 1, current_word)

            board[r][c] = temp      # Restore the original value of the cell after DFS

        # Start DFS from every cell in the board
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(trie.root, row, col, "")

        return list(result)         # Return the list of found words
