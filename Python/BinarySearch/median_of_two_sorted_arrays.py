'''

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

'''

nums1 = [1, 3]
nums2 = [2] 

m = len(nums1)
n = len(nums2)

# output should be 2 

nums1 = [1, 2]
nums2 = [3, 4] 

m = len(nums1)
n = len(nums2)

# output should be (2+3)/2 = 2.5 

class solution:

    def binarySearch(self, arr, target):
        '''
        binary search 
        inputs = array and target
        output = index target 
        '''
        left = 0 
        right = len(arr)-1
        while right <= left:
            middle = (left + right)//2
            if arr[middle] == target:
                return middle 
            elif arr[middle] < target:
                left = arr[middle]+1
            else:
                right = arr[middle]-1
            return -1 


    def findMedian(self, nums1, nums2):
        '''
        inputs two arrays of ints 
        output median value 

        nums1 = [1, 2]
        nums2 = [3, 4] 

        m = len(nums1)
        n = len(nums2)

        '''
        total = len(nums1) + len(nums2)
        half = (total) // 2 

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1 
        
        left_index = 0 
        right_index = len(nums1) - 1 
        
        while True:
            nums1_index = (left_index + right_index) // 2 
            nums2_index = half - nums1_index - 2 # -2 bc we want index 

            nums1_left = nums1[nums1_index] if nums1_index >= 0 else -1
            nums1_right = nums1[nums1_index + 1] if (nums1_index+1) < len(nums1) else 100000000

            nums2_left = nums2[nums2_index] if nums2_index >= 0 else -1 
            nums2_right = nums2[nums2_index + 1] if (nums2_index+1) < len(nums2) else 100000000

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total%2:
                    return min(nums1_right, nums2_right)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2 
            elif nums1_left > nums2_right:
                right_index = nums1_index - 1 
            else:
                left_index = nums1_index + 1 



nums1 = [1, 3]
nums2 = [2] 

m = len(nums1)
n = len(nums2)

# output should be 2 
print(solution().findMedian(nums1, nums2))


nums1 = [1, 2]
nums2 = [3, 4] 

m = len(nums1)
n = len(nums2)

print(solution().findMedian(nums1, nums2))


nums1 = [1,2,3,4,6,8,9,10,12,15,17,21]
nums2 = [2,4,7,9,12,16,21,55,100,101]

num_all = sorted(nums1 + nums2)
total_l = len(num_all)
index = len(num_all)//2 
if total_l%2:
    print(num_all[index])
else:
    print( (num_all[index-1]+num_all[index]) / 2 )


print(solution().findMedian(nums1, nums2))
