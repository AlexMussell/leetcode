class Solution:
    def reverse(self, x):
        INT32_MAX = 2 ** 31 - 1
        INT32_MIN = -2 ** 31
        INT32_MAX_DIV_10 = INT32_MAX / 10
        
        sign = 1 if x >= 0 else -1
        x = abs(x)

        result = 0

        while x:
            x, digit = divmod(x, 10)
            if result > INT32_MAX_DIV_10 or (result == INT32_MAX_DIV_10 and digit > 7):
                return 0
            result = result * 10 + digit

        return result * sign


solution = Solution()

print(solution.reverse(12345))