# Def: A permutation is an ordered arragement of objects or numbers 
def construct_beautiful_permutation(n):
	if n == 1:
		return '1'
	if n < 4:
		return 'NO SOLUTION'

	i = 0
	rs = []
	while (i + 2) <= n:
		i += 2
		rs.append(i)
	
	for i in range(len(rs)):
		rs.append(rs[i] - 1)
	
	if n % 2 != 0:
		rs.append(n)
	
	return ' '.join(map(str, rs))
	
user_n = int(input())
print(construct_beautiful_permutation(user_n))