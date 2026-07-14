class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l= s.split()
        list1=[]
        for i in range( len(l)-1,-1,-1):
            list1.append(l[i])

        x= ' '.join(list1)
        return x
        
