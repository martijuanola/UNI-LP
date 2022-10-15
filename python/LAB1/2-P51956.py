########################################

def myLength(l):
	count = 0
	for e in l:
		count += 1
	return count
	#return len(l)


########################################

def myMaximum(l):
	maximum = l[0]
	for e in l:
		if e > maximum:
			maximum = e
	return maximum
	#return max(l)


########################################

def average(l):
	sum = 0
	for e in l:
		sum += e
	return sum / len(l)


########################################

def buildPalindrome(l):
	return l[::-1] + l
	#return [*l[::-1], *l]
	#...


########################################

def remove(l1, l2):
	return [x for x in l1 if not x in l2]


########################################

def flatten(l):
	l2 = []
	for sl in l:
		if type(sl) != list:
			l2.append(sl)
		else:
			l2 += flatten(sl)
	return l2


########################################

def oddsNevens(l):
	return ([o for o in l if o % 2 != 0], [e for e in l if e % 2 == 0])


########################################

def primeDivisors(n):
	return [d for d in range(2, n+1) if n % d == 0 and isPrime(d)]

def isPrime(n):
    if n < 2: return False
    for d in range(2, n):
        if n % d == 0: return False
    return True
    #return not len([x for x in range(2,n) if n % x == 0]) > 0


########################################

