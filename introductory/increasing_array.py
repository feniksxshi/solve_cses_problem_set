def find_min_moves(nums):
	moves = 0
	i, j = 0, 1
	while j < len(nums):
		if nums[j] < nums[i]:
			moves += nums[i] - nums[j]
		else:
			i = j
		j += 1 
	
	return moves 

user_n = int(input())
user_nums = input()
nums = [int(n) for n in user_nums.split()]

print(find_min_moves(nums))