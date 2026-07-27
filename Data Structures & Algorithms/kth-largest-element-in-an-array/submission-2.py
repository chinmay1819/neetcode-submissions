class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ind_store = set()
        size_of_nums = len(nums)
        current_max:int = nums[0]
        ind = 0

        while k > 0:
            current_max = -100000
            for i in range(0,size_of_nums):
                if i not in ind_store and nums[i] > current_max: 
                    current_max = max(current_max,nums[i])
                    ind = i

            ind_store.add(ind)
           
            k -= 1

        
        return current_max