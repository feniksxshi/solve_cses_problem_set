def main():
	n = int(input())
	if not n:
		return 
	
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

output = main()
for num in output:
	print(f"{num:.0f}")