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

def rob(nums):
    def rob_row(nums):    
        money = [0]*len(nums)
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            money[i] = max(money[i-1], money[i-2] + nums[i])
        return money[-1]
    if not nums: 
        return 0
    if len(nums) <= 2: 
        return max(nums)
    return max(rob_row(nums[1:]), rob_row(nums[:-1]))    
