class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        count = 0 
        for i in nums:
            if i == 1:
                count += 1
            else:
                max_consecutive_ones = max(max_consecutive_ones, count)
                count = 0
        return max(max_consecutive_ones, count)
        