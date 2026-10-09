class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []

        for ch in s:
            if ch.isdigit():
                digits.append(int(ch))

        digits = sorted(set(digits), reverse=True)

        if len(digits) < 2:
            return -1

        return digits[1]
        