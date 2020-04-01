def main():
    a = [10211,4, 7, 12, 89, 1, 100]
    size = len(a)
    bubble(a, size)


def bubble(a, size):
    for i in range(1,size):
        flag = 0
        for j in range(size-i):
            if a[j] > a[j+1]:
                flag = 1
                a[j], a[j+1] = a[j+1], a[j]
        if flag == 1:
            break
    print(a)
main()