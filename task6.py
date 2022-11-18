## Сложность алгоритма O(n)
def rob(nums):
    def checker_rob(nums):
        suc = 0
        not_suc = 0
        for num in nums:
            suc , not_suc = not_suc + num , max(not_suc,not_suc)
        return max(suc,not_suc)    
    if len(nums) == 1:
        return nums[-1]
    elif not nums:
        return 0
    else:
        return max(checker_rob(nums[1:]),checker_rob(nums[:-1]))