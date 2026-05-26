### 27.05.2026 
I have been getting confused about setting conditions to terminate a loop, here is one example:
```python
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
```
I should set condition for `i` or `j`, `len(nums)` or `len(nums) - 1` ... 
- [ ] Clear yet?
