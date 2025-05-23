from typing import List

# Trie Node definition
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

# Trie implementation
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert word into the Trie
    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.word_end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Step 1: Build Trie from word dictionary
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        memo = {}  # Memoization dictionary

        # Step 2: Backtracking function with memoization
        def backtrack(index):
            if index in memo:
                return memo[index]

            result = []
            node = trie.root

            for j in range(index, len(s)):
                char = s[j]
                if char not in node.children:
                    break
                node = node.children[char]

                if node.word_end:
                    current_word = s[index:j + 1]
                    if j + 1 == len(s):  # Entire string used
                        result.append(current_word)
                    else:
                        for suffix in backtrack(j + 1):
                            result.append(current_word + " " + suffix)

            memo[index] = result
            return result

        return backtrack(0)
