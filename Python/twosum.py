

nums = [2,7,11,15]
target = 9


def twoSums(nums, target):
	for i, elem in enumerate(nums):
		n = target - elem 
		for j, elem2 in enumerate(nums):
			if elem2 == n and i != j:
				return [i, j]
	return False 


result = twoSums(nums, target)

print(result)


nums = [3,4,7,2]
target = 6


result = twoSums(nums, target)
print(result)	

#---- 


def twoSumsOpt(nums, target):
	d = {} 
	for i, elem in enumerate(nums):
		needed_n = target - elem 
		if needed_n in d:
			return [d[needed_n], i]
		d[elem] = i
	return []


nums = [3,4,7,2]
target = 6


result = twoSumsOpt(nums, target)
print(result)
 
	
		
				
		 



