def merge_sort(x):
    if len(x) <= 1:
        return x

    middle = len(x) / 2
    return merge(merge_sort(x[:middle]), merge_sort(x[middle:]))

def merge(left, right):
    result = []
    i = j = 0
    while(len(left) > i and len(right) > j):
        if left[i] < right[j]:
                result.append(left[i])
                i += 1
        else:
                result.append(right[j])
                j += 1
    result += left[i:]
    result += right[j:]
    return result
