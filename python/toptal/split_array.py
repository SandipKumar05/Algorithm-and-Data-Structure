def find_index_with_equal_counts(X, A):
    count_equal_to_X = 0
    count_different_from_X = len(A)-A.count(X)
    for K in range(len(A)):
        if A[K] == X:
            count_equal_to_X += 1
        else:
            count_different_from_X -= 1
        if count_equal_to_X == count_different_from_X:
            return K
    return -1
X = 5
A = [5, 5, 1, 7, 2, 3, 5]
result = find_index_with_equal_counts(X, A)
print(result)
