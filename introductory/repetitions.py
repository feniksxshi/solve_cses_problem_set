# 2 pointers technique
def find_max_length_repetition(dna):
	l, r, length, max_length = 0, 0, 0, 0
	while r != len(dna):
		if dna[l] != dna[r]:
			l = r
			length = 1
		else:
			length += 1
			max_length = max(max_length, length)
		
		r += 1

	return max_length 

user_input = input() # 'ATTCGGGA'
check = True
for c in user_input:
	if c not in ('A', 'C', 'G', 'T'):
		check = False
		break

if check == True:
	print(find_max_length_repetition(user_input))
