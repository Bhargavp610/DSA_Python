class Solution(object):
    def twoSum(self, nums, target):
            traversed = {}
            for i in range(len(nums)):
                complement = target - nums[i]
                if complement in traversed:
                    return [traversed[complement], i]
                traversed[nums[i]] = i
            return []
        