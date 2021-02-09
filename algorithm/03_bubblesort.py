def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):

        # 한 단계마다 정렬은 마지막 요소가 되므로
        # i 를 4, 3, 2, 1, 0으로 만들어서 범위를 잡아주자
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        return a


numbers = BubbleSort([55, 7, 78, 12, 42])
print(numbers)
