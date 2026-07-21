class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n= len(word1)
        m= len(word2)
        q= []
        if n>m:
            for i in range(m):
                q.append(word1[i])
                q.append(word2[i])
            for i in range(m, n, 1):
                q.append(word1[i])
        else:
            for i in range(n):
                q.append(word1[i])
                q.append(word2[i])
            for i in range(n, m, 1):
                q.append(word2[i])           
        x= ''.join(q)
        return x


     
