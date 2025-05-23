from collections import defaultdict

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # Early exit if valueDiff is negative, which is invalid
        if valueDiff < 0:
            return False

        # Dictionary to hold the current sliding window buckets
        buckets = {}
        # Bucket width to separate values that are guaranteed to differ by more than valueDiff
        bucket_size = valueDiff + 1

        for i, number in enumerate(nums):
            # Determine the bucket ID for the current number
            bucket_id = number // bucket_size

            # Check if the number already exists in the same bucket
            if bucket_id in buckets:
                return True

            # Check the left neighbor bucket for a valid match
            if (bucket_id - 1 in buckets and 
                abs(number - buckets[bucket_id - 1]) <= valueDiff):
                return True

            # Check the right neighbor bucket for a valid match
            if (bucket_id + 1 in buckets and 
                abs(number - buckets[bucket_id + 1]) <= valueDiff):
                return True

            # Insert the current number into its bucket
            buckets[bucket_id] = number

            # Remove the number that is now out of the sliding window range
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket_id]

        return False