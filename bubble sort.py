def main():
    a = [10211,4, 7, 12, 89, 1, 100]
    size = len(a)
    bubble(a, size)


def bubble(a, size):
    for i in range(1,size):
        for j in range(size-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    print(a)
main()