class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)


solution = Solution()

print(solution.maxSubArray([1, -1, -3, 6, 3, -1, 2, 3]))
