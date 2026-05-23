def handle_weird_algorithm(n):
	i = n
	rs = [n]
	while i != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = n * 3 + 1
		i = n
		rs.append(i) 
	
	return rs

n = int(input())
output = handle_weird_algorithm(n)
for num in output:
	print(f"{num:.0f}")