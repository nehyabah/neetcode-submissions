class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []                # This will store our result triplets
        nums.sort()             # Step 1: Sort the list

        for i in range(len(nums)):
            # Step 2: Skip duplicates (we’ve already checked this number)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Two pointers
            left = i + 1             # Start one pointer just after i
            right = len(nums) - 1    # Start the other pointer at the end

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # Found a triplet!
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates on the left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates on the right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers in
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # We need a bigger number
                else:
                    right -= 1  # We need a smaller number

        return res
