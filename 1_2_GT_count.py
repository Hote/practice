class Solution:
    def findTest(self,numsA,numsB):
        """
        :type numsA: List[int]
        :type numsB: List[int]
        :rtype: List[int]
        """
        #length=len(list)
        if (len(numsA) < len(numsB)):
            return self.findTest( numsB, numsA)


        count=0
        aCount=[]


        for i in range(len(numsA)):
            length = 0
            for j in range(len(numsB)):

                if numsA[i]>numsB[j]:
                    next
                else:
                    length=length+1
            print("length==",length)
            count = len(numsA) - length
            aCount.append(count)

            #count=len(numsA)-length
            #print(count)
        #return sorted_list[length]
        return aCount

#nums=[1,2,2,3,3,3,3,4,5,5,6]
numsA=[1,3,5,7,9]
numsB=[2,3,4,7,8]


result=Solution().findTest(numsA,numsB)
print(result)