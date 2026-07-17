class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        low=mid= float('inf')
        for i in nums:
            if i<=low:
                low=i
            elif i<= mid:
                mid=i    
            else:
                return True
        else:
            return False




