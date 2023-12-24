class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #DEBUG = False

        nums_map = {}

        target_idx = [-1, -1]

        n = len(nums)

        for i, num in enumerate(nums):

            left_target = target - num

            #print(i, num, nums_map) if DEBUG else None

            if left_target in nums_map:
                
                target_idx = [i, nums_map[left_target]]
                break

            nums_map[num] = i

        return target_idx

        
