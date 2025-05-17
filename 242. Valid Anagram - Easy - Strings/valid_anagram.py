from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use Counter to count character frequencies in both strings
        # Compare if both Counters are equal (same characters with same counts)
        return Counter(s) == Counter(t)
