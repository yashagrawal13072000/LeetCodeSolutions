# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        
        n = len(arr)
        i = 0
        while i < n-1 and arr[i]<arr[i+1]:
            i += 1
        
        if i == 0 or i == n-1:
            return False
        
        while i < n - 1 and arr[i]>arr[i+1]:
            i += 1

        return i == n-1
        
        