# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def bt(index, current_sum):
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
        
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            positive = bt(index+1, current_sum + nums[index])
            negative = bt(index+1, current_sum - nums[index])

            memo[(index, current_sum)] = positive + negative

            return memo[(index, current_sum)]
        return bt(0,0)