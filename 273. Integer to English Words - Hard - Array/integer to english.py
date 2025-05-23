class Solution:
    def numberToWords(self, number: int) -> str:
        if number == 0:
            return "Zero"

        # Arrays to map numbers to words
        words_below_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
            "Seventeen", "Eighteen", "Nineteen"
        ]

        words_tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        place_values = ["", "Thousand", "Million", "Billion"]

        def convertThreeDigits(n: int) -> str:
            if n == 0:
                return ""
            elif n < 20:
                return words_below_20[n] + " "
            elif n < 100:
                return words_tens[n // 10] + " " + convertThreeDigits(n % 10)
            else:
                return words_below_20[n // 100] + " Hundred " + convertThreeDigits(n % 100)

        result = ""
        for idx, place in enumerate(place_values):
            if number % 1000 != 0:
                chunk = convertThreeDigits(number % 1000)
                result = chunk + place + " " + result
            number //= 1000

        return result.strip()
