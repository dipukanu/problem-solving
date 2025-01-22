# Top K Frequent Elements

# The goal is to return the 'k' most frequent elements from a given list of numbers.

# Examples:
# 1. Input: nums = [1, 1, 1, 2, 2, 3], k = 2
#    Output: [1, 2]
#    Explanation: The numbers 1 and 2 are the two most frequently occurring elements in the list.

# 2. Input: nums = [3, 0, 1, 0], k = 1
#    Output: [0]
#    Explanation: The number 0 appears more frequently than any other number in the list.

nums = [1, 1, 1, 2, 2, 3]
k = 2


class Solution(object):
    def topKFrequent(self, nums, k):
        # Define an empty dictionary
        num_count = {}
        for num in nums:
            # If number does not exist in dict
            # add the number, else update the count of the value
            if not num_count.get(num):
                num_count[num] = 1
            else:
                num_count[num] += 1
        # Sort the keys based on their values count
        result = sorted(num_count.keys(), key=lambda x: num_count[x], reverse=True)
        # Return the K frequent elements
        return result[:k]


# Create an instance and call the topKFrequent method with args
obj = Solution()
obj.topKFrequent(nums, k)
