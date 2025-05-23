class TrieNode:
    def __init__(self):
        # Dictionary mapping character to child TrieNode
        self.children = {}
        # Flag to mark the end of a complete word
        self.is_word_end = False


class Trie:
    def __init__(self):
        # Root node of Trie does not hold any character
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start traversal from root
        current_node = self.root
        for char in word:
            # Create new child node if character not found
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            # Move to the child node
            current_node = current_node.children[char]
        # Mark the last node as a complete word end
        current_node.is_word_end = True

    def search(self, word: str) -> bool:
        # Start traversal from root
        current_node = self.root
        for char in word:
            # If char path does not exist, word not found
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # Return True only if current node marks the end of a word
        return current_node.is_word_end

    def startsWith(self, prefix: str) -> bool:
        # Start traversal from root
        current_node = self.root
        for char in prefix:
            # If char path does not exist, prefix not found
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # If all chars found, prefix exists
        return True


# Example usage:
# trie = Trie()
# trie.insert("apple")
# print(trie.search("apple"))   # True
# print(trie.search("app"))     # False
# print(trie.startsWith("app")) # True
# trie.insert("app")
# print(trie.search("app"))     # True
