class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        a = 0  

        for b in range(1, len(nums)):  
            if nums[b] != nums[a]:
                a += 1
                nums[a] = nums[b]

        return a + 1