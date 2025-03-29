nums = [1, 3, 5, 6, 9]
target = 8
class Solution:
    def twoSum(self, nums, target):
        # store the number and its corresponding index
        pre_value = {}

        for i, n in enumerate(nums):
            x = target - n
            # if the difference is already in dictionary, return the indices
            if x in pre_value:
                # pre_value[x] gives the index of the number that sums with n to form target
                # i gives the current index of n
                return [pre_value[x], i]
            # store the current number and  its index in dictionary
            pre_value[n]=i

obj = Solution()
obj.twoSum(nums, target)
