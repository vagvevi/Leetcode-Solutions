class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge case: If there are no houses
        if n == 0:
            return 0
        
        # Edge case: If there is only one house
        if n == 1:
            return nums[0]
        
        # Edge case: If there are two houses, choose the maximum value
        if n == 2:
            return max(nums[0], nums[1])
        
        # Dynamic Programming array to store the maximum money that can be robbed up to each house
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Fill in the dp array based on the recurrence relation
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        # The last element in dp array contains the maximum money that can be robbed
        return dp[-1]
        