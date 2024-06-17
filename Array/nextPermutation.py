class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # check 
        n = len(nums)
        if n == 0:return
        k = n-2

        for i in range(n-1,0,-1):
            if nums[k] > nums[i]:
                k-=1
        
        if k == -1:
            self.reverse_index(0,n-1)
        else:
            self.reverse_index(k,n-1)
        



        

    def reverse_index(self,start,end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1



nums = [3,1,4,2]
s = Solution()
print(s.nextPermutation(nums))
# print(s.reverse_index(nums,0,len(nums)-1))
print(nums)