def solution(A):
    setA = set(A)

    min_int = 1

    while min_int in setA:
        min_int += 1

    return min_int


print(solution([1, 3, 6, 4, 1, 2]))
print('==')
print(solution([1, 2, 3]))
print('==')
print(solution([-1, -3]))