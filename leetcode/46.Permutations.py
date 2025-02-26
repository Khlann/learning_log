from typing import List

# def backtracking(nums:List[int], level: int, permutations:List[List[int]]):
#     if level == len(nums) - 1:
#         permutations.append(nums[:])
#         return
#     for i in range (level, len(nums)):
#         nums[i],nums[level] = nums[level], nums[i]
#         backtracking(nums, level+1, permutations)
#         nums[i], nums[level] = nums[level], nums[i]

# def permute(nums: List[int]):
#     permutations =[]
#     backtracking(nums, 0, permutations)
#     return permutations

# input = [1,2,3]

# print(permute(input))


def backtracking(list, level, result):
    if level == len(list)-1:
        result.append(list[:])
        return
    for i in range(level, len(list)):
        list[i], list[level] = list[level], list[i]
        backtracking(list, level+1, result)
        list[level], list[i] = list[i], list[level]
    return result

def permutation(list):
    result = []
    backtracking(list, 0, result)
    return result

input = [1,2,3]

print(permutation(input))
