class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums1 = sorted(set(nums))

        current = 1
        longest = 1

        for i in range(1, len(nums1)):
            if nums1[i] == nums1[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)
