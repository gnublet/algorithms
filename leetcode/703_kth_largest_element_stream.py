from typing import *
import heapq
import itertools

class KthLargest:
    # make the 0th element correspond to the kth largest element
    # Use a min-heap
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        # pop until you're left with k largest elements
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)    
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0] # the kth largest element
