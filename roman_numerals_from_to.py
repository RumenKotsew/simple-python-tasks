class RomanNumerals:

    number_2_roman = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    roman_2_number = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    @staticmethod
    def to_roman(val):
        result = ''

        for i, k in enumerate(RomanNumerals.number_2_roman):
            v = val // k
            if v == 4 and k != 1000:
                result += RomanNumerals.number_2_roman[k]
                result += RomanNumerals.number_2_roman[list(RomanNumerals.number_2_roman)[(i or 1) - 1]]
            else:
                result += RomanNumerals.number_2_roman[k] * v

            val %= k

        result = result.replace('DCD', 'CM')
        result = result.replace('LXL', 'XC')
        result = result.replace('VIV', 'IX')
        return result

    @staticmethod
    def from_roman(val):
        result = 0
        last = 0
        for i in val[::-1]:
            current = RomanNumerals.roman_2_number[i]
            if current < last:
                result -= current
            else:
                result += current
            last = current
        return result
