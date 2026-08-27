class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            i = abs(num) - 1
            if nums[i] > 0:
                nums[i] = -nums[i]

        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans