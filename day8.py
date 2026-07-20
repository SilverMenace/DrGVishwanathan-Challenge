class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        orig= list(s)
        vowels= ['a','e','i','o','u','A','E','I','O','U']
        mod= [x for x in orig if x in vowels]
        mod1=mod[::-1]
        j=0
        for i in range(len(orig)):
            if orig[i] in vowels:
                orig[i]=mod1[j]
                j+=1
        return ''.join(orig)
