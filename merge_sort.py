def main():
	a = [10000, 12, 8,10,16,45,45,45,1,0,0]
	beg = 0
	end = len(a)-1
	print(a)
	merge_sort(a,beg,end)
	print(a)

def merge(a,beg,end,mid):
	i = beg
	j = mid+1
	index = 0
	k = 0
	temp = []
	while i<=mid and j<=end:
		if a[i] < a[j]:
			temp.append(a[i])
			i+=1
		else:
			temp.append(a[j])
			j+=1
		index+=1

	if i > mid:
		while j<=end:
			temp.append(a[j])
			index+=1
			j+=1
	else:
		while i<=mid:
			temp.append(a[i])
			i+=1
			index+=1 
	while k<index:
		a[k+beg] = temp[k]
		k+=1

def merge_sort(a,beg,end):
	if beg<end:
		mid = (beg+end)//2
		merge_sort(a,beg,mid)
		merge_sort(a,mid+1,end)
		merge(a,beg,end,mid)

main()




