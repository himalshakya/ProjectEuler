def problem1(num):
	numlist = []
	for i in range(1,num):
		if i % 3 == 0 or i % 5 == 0:
			if i not in numlist:
				numlist.append(i)

	return sum(numlist)

print problem1(1000)