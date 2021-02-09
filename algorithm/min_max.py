T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_num = nums[0]
    min_num = nums[0]
    result = 0
    for i in range(0, len(nums)):
        if max_num < nums[i]:
            max_num = nums[i]

        if min_num > nums[i]:
            min_num = nums[i]

    result = max_num - min_num

    print(f'#{tc} {result}')
