class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []  # Stores all possible palindrome partitions

        def is_palindrome(substring: str) -> bool:
            # Check if the substring is a palindrome
            return substring == substring[::-1]

        def backtrack(start_index: int, current_partition: List[str]) -> None:
            # If we've reached the end of the string, add the current partition to the result
            if start_index == len(s):
                result.append(current_partition[:])  # Append a copy of current partition
                return
            
            # Try all possible substrings starting from start_index
            for end_index in range(start_index + 1, len(s) + 1):
                substring = s[start_index:end_index]
                
                # If the substring is palindrome, include it in the current partition and recurse
                if is_palindrome(substring):
                    current_partition.append(substring)
                    backtrack(end_index, current_partition)
                    current_partition.pop()  # Backtrack: remove the last substring added
        
        # Start backtracking from index 0 with an empty current partition
        backtrack(0, [])
        return result
