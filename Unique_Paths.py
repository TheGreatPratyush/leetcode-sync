# Unique Paths
# Platform: LeetCode
# Language: Python3

class Solution:
    def generate_subsequence(self,index,nums,subset,result,k):
        if len(subset)==k:
            result.append(subset[:])
            return 
        if index>=len(nums):
            return 
        subset.append(nums[index])
        self.generate_subsequence(index+1,