class Solution:
    def isPalindrome(self, n):
        """(n: int) -> bool"""
        x, y = n, 0
        f = lambda: (y * 10) + x % 10
        while x > 0:
            x, y = x//10, f()
        return y == n


solution = Solution()

print(solution.isPalindrome(12345))
print(solution.isPalindrome(12321))
