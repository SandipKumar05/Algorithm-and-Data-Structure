
def equal_sum(arr):
    total = sum(arr)
    temp_sum = 0
    for i in arr:
        temp_sum += i
        if temp_sum == total/2:
            return True
        elif temp_sum > total/2:
            return False
    return False
