""" 
  quickselect algorithm described in  Introduction to Algorithm Sec9.2
  a: a given list
  k: k-th minimum number from the list a
  Liangyue Li (jackiey99@gmail.com)
"""

def quickselect(a, k):
	if a==[]:
		return []
	if len(a)==1:
		return a
	else:
		pivot = a[0]
		left = [x for x in a if x < pivot]
		right = [x for x in a[1:] if x >= pivot]
		if(len(left)+1 == k):
			return pivot
		if(len(left)+1 > k):
			return quickselect(left,k)
		else:
			return quickselect(right,k-len(left)-1)
