class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)

        while start < end:
            
            mid = (end + start)//2

            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                end = mid
            else:
                start = mid+1
        
        return -1
            

        