def main():
    a = [178675, 4, 10, 0, 21, 15577, 534]
    n = len(a)
    selection_sort(a, n)

def selection_sort(a,n):
	for i in range(n):
		min = i
		for j in range(i+1,n):
			if a[j]< a[min]:
				min = j

		a[min],a[i] = a[i],a[min]
	print(a)
main()
