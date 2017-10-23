def merge_sort(list_entry):
    L = list_entry[:]
    for i in range(1, len(L)):
        for j in range(i, 0, -1):
            if L[j] < L[j - 1]:
                L[j], L[j - 1] = L[j - 1], L[j]
    return L


def divide_sort(list_entry):
    L = []
    if len(list_entry) <= 1:
        return list_entry
    if len(list_entry) == 2:
        if list_entry[0] > list_entry[1]:
            return list_entry[::-1]
        else:
            return list_entry
    lefts = heap_sort(list_entry[:len(list_entry) / 2])
    rights = heap_sort(list_entry[len(list_entry) / 2:])
    while len(lefts) + len(rights) > 0:
        if len(lefts) == 0:
            L += rights
            break
        if len(rights) == 0:
            L += lefts
            break
        if lefts[0] > rights[0]:
            element = rights.pop(0)
        else:
            element = lefts.pop(0)
        L.append(element)
    return L


def return_sorted_list(L1, L2):
    L = []
    while len(L1) > 0 and len(L2) > 0:
        if L1[0] > L2[0]:
            element = L1.pop(0)
        else:
            element = L2.pop(0)
        L.append(element)
    if len(L1) == 0:
        L += L2
    elif len(L2) == 0:
        L += L1
    return L


def non_recursive_divide_sort(list_entry):
    L = list_entry[:]
    tmpIndex = 2
    while tmpIndex < len(L):
        for i in range(0, len(L), tmpIndex):
            L2 = return_sorted_list(L[i:i + tmpIndex / 2], L[i + tmpIndex / 2:i + tmpIndex])
            L[i:i + tmpIndex] = L2
        tmpIndex *= 2
    L = return_sorted_list(L[tmpIndex / 2:], L[tmpIndex / 2:])
    return L


def quick_sort(L):
    L = L[:]
    if len(L) > 1:
        half = L[-1]
        l, r = 0, 0
        for i in range(len(L) - 1):
            if L[i] < half:
                L[r], L[l] = L[l], L[r]
                l += 1
            r += 1
        L[-1], L[l] = L[l], L[-1]
        left = quick_sort(L[:l])
        right = quick_sort(L[l + 1:])
        L = left + [L[l]] + right
    return L