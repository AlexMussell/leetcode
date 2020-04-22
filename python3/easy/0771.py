class Solution:
    def numJewelsInStones(self, J, S):
        """J: str, S: str -> int"""
        charFreq = {}
        count = 0

        for char in S:
            if char not in charFreq:
                charFreq[char] = 1
            else:
                charFreq[char] += 1

        for char in J:
            if char in charFreq:
                count += charFreq[char]

        return count


solution = Solution()

print(solution.numJewelsInStones("Aa", "aAabcAd"))

