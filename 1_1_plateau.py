class Solution:
    def findPlate(self,list):
        """
        :type nums: List[int]
        :rtype: int
        """
        #length=len(list)
        sorted_list=sorted(list)
        length=1
        for i in range(len(sorted_list)):

            if(sorted_list[i]==sorted_list[i-length]):
                length=length+1
        return sorted_list[length]


#nums=[1,2,2,3,3,3,3,4,5,5,6]
nums=[10,9,3,5,7,19,12,7]


result=Solution().findPlate(nums)
print(result)