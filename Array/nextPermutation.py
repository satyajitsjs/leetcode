class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        # check  
        if n == 0:return
        k = n-2

        # Set K
        for i in range(n-1,0,-1):
            if nums[k] >= nums[i]:
                k -= 1
            else:
                break
        
        if k == -1:
            self.reverse_index(nums,0,n-1)
            return
        else:
            # replace the k with next greater element
            for i in range(n-1,0,-1):
                if nums[i] > nums[k]:
                    temp = nums[k]
                    nums[k] = nums[i]
                    nums[i] = temp
                    break
            self.reverse_index(nums,k+1,n-1)
        


    def reverse_index(self,nums,start,end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1



nums = [5,1,1]
s = Solution()
print(s.nextPermutation(nums))
# print(s.reverse_index(nums,0,len(nums)-1))
print(nums)