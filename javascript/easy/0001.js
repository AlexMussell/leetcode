const twoSum = (nums,target) => {
    const seen = {};

    for (let i = 0; i < nums.length; i++) {
        if (seen[nums[i]] >= 0) {
            return [seen[nums[i]], i]
        }
        seen[target - nums[i]] = i
    }
};

twoSum([2, 7, 11, 15], 9);
