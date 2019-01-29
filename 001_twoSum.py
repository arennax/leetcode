class Solution:
    def twoSum (self, nums, target):
        temp_link = {}
        # note must use "{}", not "[]"
        for i in range(len(nums)):
            if nums[i] in temp_link:
                return [temp_link[nums[i]], i]
            else:
                temp_link[target - nums[i]] = i
