def findMInandMax(L):
    if L == []:
        return (None, None)
    else:
        mins, maxs = L[0], L[0]
        for min in L:
            if min < mins:
                mins = min
        for max in L:
            if max > maxs:
                maxs = max
        return (mins, maxs)


print(findMInandMax([]))
print(findMInandMax([7, 1, 3, 9, 5]))
