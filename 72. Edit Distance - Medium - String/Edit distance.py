class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1, len_word2 = len(word1), len(word2)
        
        # prev_row[j]: min edit distance between first i-1 chars of word1 and first j chars of word2
        prev_row = list(range(len_word2 + 1))
        # curr_row[j]: min edit distance between first i chars of word1 and first j chars of word2
        curr_row = [0] * (len_word2 + 1)

        for i in range(1, len_word1 + 1):
            curr_row[0] = i  # converting first i chars of word1 to empty word2 requires i deletions
            
            for j in range(1, len_word2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match, no additional operation needed
                    curr_row[j] = prev_row[j - 1]
                else:
                    # Minimum of:
                    # 1. Deletion (prev_row[j] + 1)
                    # 2. Insertion (curr_row[j - 1] + 1)
                    # 3. Replacement (prev_row[j - 1] + 1)
                    curr_row[j] = 1 + min(
                        prev_row[j],      # Delete character from word1
                        curr_row[j - 1],  # Insert character into word1
                        prev_row[j - 1]   # Replace character
                    )
            
            prev_row, curr_row = curr_row, prev_row  # Swap rows for next iteration

        return prev_row[len_word2]
