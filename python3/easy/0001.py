class Solution:
    def twoSum(self, nums, target):
        """(List[int], int) -> List[int] """

        seen = {}
        for position, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining], position]
            seen[num] = position
        return []

        
solution = Solution()

print(solution.twoSum([2,3,4,11,15], 9))