class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        occurrences = {}
        for num in nums:
            if num in occurrences:
                occurrences[num] += 1  
            else:
                occurrences[num] = 1  
        for count in occurrences.values():
            if count>1:
                return True
        return False