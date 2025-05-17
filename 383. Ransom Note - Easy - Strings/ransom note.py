from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count frequency of each character in ransomNote and magazine
        ransom_note_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        
        # For each character in ransomNote, check if magazine has enough of it
        for char in ransom_note_counter:
            if ransom_note_counter[char] > magazine_counter[char]:
                return False  # Not enough characters to construct ransomNote
        return True  # All characters are sufficiently present
