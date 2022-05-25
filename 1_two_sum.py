from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            rem = target - num
            
            if rem in table:
                return table[rem], i
            
            table[num] = i
            

if __name__ == "__main__":
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == (0, 1)
    assert solution.twoSum([3, 2, 4], 6) == (1, 2)
    assert solution.twoSum([3, 3], 6) == (0, 1)