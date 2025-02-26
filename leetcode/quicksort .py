import random
def quicksort(nums,l,r):
    # l , r = 0 , len(arr) - 1
    if l >= r:
        return
    pivot = random.randint(l,r)
    pivot_val = nums[pivot]
    nums[l],nums[pivot] = nums[pivot],nums[l]
    i , j = l+1 , r
    while True:
        while i < r and nums[j]>=pivot_val:
            j -= 1
        while i < j and nums[i]<=pivot_val:
            i += 1
        if i == j:
            break
        nums[i] , nums[j] = nums[j] , nums[i]
    
    new_pivot =  i if nums[i]<=nums[l] else i-1
    nums[l],nums[new_pivot] = nums[new_pivot],nums[l]
    quicksort(nums,l,new_pivot-1)
    quicksort(nums,new_pivot+1,r)
    
if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    quicksort(nums,0,len(nums)-1)
    print(nums)
    