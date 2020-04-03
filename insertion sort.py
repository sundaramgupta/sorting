def main():
    a = [1, 4, 10, 0, 21, 15577, 534]
    n = len(a)
    insertion_sort(a, n)


def insertion_sort(a, n):
    for i in range(1, n):
        temp = a[i]
        hole = i
        while hole > 0 and temp < a[hole - 1]:
            a[hole] = a[hole - 1]
            hole = hole - 1
        a[hole] = temp
    print(a)


main()
