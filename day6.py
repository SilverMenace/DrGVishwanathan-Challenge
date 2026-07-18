class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        t=0
                    

        for i in range(len(flowerbed)):
            if len(flowerbed)==1:
                if flowerbed[0]==0:
                    t+=1
                    break

            if flowerbed[0]==0 and flowerbed[1]==0:
                t+=1
                flowerbed[0]=1
            if flowerbed[-1]==0 and flowerbed[-2]==0:
                t+=1
                flowerbed[-1]=1
            if flowerbed[i]!=1 and flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
                t+=1
                flowerbed[i]=1 
        if t>=n:
            return True
        else:
            return False
