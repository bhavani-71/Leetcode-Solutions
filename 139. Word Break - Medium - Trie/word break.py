from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end_of_word = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Build the Trie using wordDict
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        memo = {}  # Cache for DFS results

        def dfs(index: int) -> bool:
            # Base case: reached the end of the string
            if index == len(s):
                return True
            
            # Return cached result if available
            if index in memo:
                return memo[index]
            
            node = trie.root
            for i in range(index, len(s)):
                ch = s[i]
                if ch not in node.children:
                    break  # Early termination if prefix doesn't exist
                node = node.children[ch]
                
                # If a word ends here, check recursively the suffix
                if node.end_of_word and dfs(i + 1):
                    memo[index] = True
                    return True
            
            memo[index] = False  # No valid segmentation from this index
            return False

        return dfs(0)
