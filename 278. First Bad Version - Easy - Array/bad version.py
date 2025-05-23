class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Finds the first bad version among versions 1 to n using binary search.

        Args:
            n (int): The total number of versions.

        Returns:
            int: The version number of the first bad version.
        """

        l, h = 1, n  # Initialize left and right pointers
        while l < h:
            mid = (l + h) // 2  # Middle version
            if isBadVersion(mid):  # If mid is bad, the first bad version is at mid or before
                h = mid
            else:
                l = mid + 1  # Else, move right to search after mid
        return l  # Left pointer will be at first bad version
