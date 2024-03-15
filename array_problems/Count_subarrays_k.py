
from collections import defaultdict

def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr) # size of the given array.
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0

    mpp[0] = 1 # Setting 0 in the map.
    for i in range(n):
        # add current element to prefix Sum:
        preSum += arr[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
        mpp[preSum] += 1

    return cnt


# if __name__ == '__main__':
#     arr = [3, 1, 2, 4]
#     k = 6
#     cnt = findAllSubarraysWithGivenSum(arr, k)
#     print("The number of subarrays is:", cnt)

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0: 1}

        prefix_sum = 0
        ans = 0 
        for n in nums:
            prefix_sum += n
            if prefix_sum - k in prefix_map:
                ans += prefix_map[prefix_sum - k]
            
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return ans
    
if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    k = 6
    obj = Solution()
    cnt = obj.subarraySum(arr, k)
    print("The number of subarrays is:", cnt)