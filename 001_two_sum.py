# -*- coding:utf-8 -*-
class Solution(object):
    """
    找到下标
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """


def two_sum(self, nums, target):
    # 健壮性
    if len(nums) <= 1:
        return False
    buff_dict = {}
    # 遍历len(nums)次
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i


if __name__ == '__main__':
    obj = Solution()
    print obj.two_sum([1, 2, 3, 4], 6)
if __name__ == "__main__":
    obj = Solution()
    print obj.twoSum([2, 7, 11, 15], 9)
