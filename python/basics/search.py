a=[4, 5, 6, 1, 2, 3]

def find_pivot(a, low, high):
    if low > high:
        return -1
    if high==low:
        return low
    mid=(low+high)/2

    if mid<high and a[mid]>a[mid+1]:
        return mid
    if low<mid and a[mid-1]<a[mid]:
        return mid-1
    if a[low]>=a[mid]:
        return find_pivot(a, low, mid-1)
    return find_pivot(a, mid+1, high)

def binary_search(a,low,high,key):
    if high<low:
        return -1
    if high==low:
        return low
    mid=(low+high)/2
    if a[mid]==key:
        return mid
    elif a[mid]>key:
        return binary_search(a, low, mid-1, key)
    else:
        return binary_search(a, mid+1, high, key)
high=len(a)-1
pivot=find_pivot(a, 0, high)
if pivot==-1:
    binary_search(a, 0, high, key)
elif a[pivot]==key:
    print(pivot)
elif a[0]<key:
    binary_search(a, 0, pivot-1, key)
else:
    binary_search(a, pivot+1, high, key)

