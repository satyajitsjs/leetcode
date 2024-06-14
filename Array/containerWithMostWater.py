class Solution:
    """
    You are given an integer array height of length n. 
    There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.

    Example 1:
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
    
    Example 2:
        Input: height = [1,1]
        Output: 1

    Constraints:
        n == height.length
        2 <= n <= 105
        0 <= height[i] <= 104

    """

    def maxArea(self, height: list[int]) -> int:
        """
        n = len(height)
        max_area = 0
        for i in range(n):
            for j in range(i+1,n):
                width = j - i
                current_height = min(height[i],height[j])
                area = width*current_height
                max_area = max(area,max_area)
        return max_area 
        
        # This time complexity is o(n^2) very bad code
        """

        #  Using Order of n o(n)
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the width and the minimum height
            width = right - left
            min_height = min(height[left], height[right])

            # Calculate the area and update max_area if necessary
            area = width * min_height
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area




height = [1,8,6,2,5,4,8,3,7]
s = Solution()
max_area = s.maxArea(height)
print(max_area)