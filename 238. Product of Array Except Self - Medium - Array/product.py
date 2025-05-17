class Solution:
    def productExceptSelf(self, numbers: List[int]) -> List[int]:
        result = [1] * len(numbers)

        # Prefix product: Multiply all elements to the left of current index
        prefix_product = 1
        for index in range(len(numbers)):
            result[index] = prefix_product
            prefix_product *= numbers[index]

        # Suffix product: Multiply all elements to the right of current index
        suffix_product = 1
        for index in range(len(numbers) - 1, -1, -1):
            result[index] *= suffix_product
            suffix_product *= numbers[index]

        return result
