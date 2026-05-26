def find_missing_number(n, nums):
	total_sum = n * (n + 1) / 2 
	tmp_sum = 0
	for n in nums:
		tmp_sum += n
	
	if total_sum != tmp_sum:
		return total_sum - tmp_sum 

user_n = int(input())
user_nums = input() # ex: '5 2 1 3'
nums = [int(x) for x in user_nums.split()] # split by whitespace

result = find_missing_number(user_n, nums)
print(f"{result:.0f}")