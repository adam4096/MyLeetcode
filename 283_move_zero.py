

def moveZeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] !=0:
            nums[j] = nums[i]
            if i != j:
                nums[i] = 0
            j +=  1
    return nums
print(moveZeroes([4,0,1,2,3,5,5,1]))


