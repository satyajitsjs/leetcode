class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
        return nums
        

s = Solution()
nums = [0,0,1]
a = s.moveZeroes(nums=nums)
print(a)