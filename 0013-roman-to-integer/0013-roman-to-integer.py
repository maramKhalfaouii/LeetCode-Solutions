class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                num -= roman_to_int[s[i]]
            else:
                num += roman_to_int[s[i]]
        return num


        