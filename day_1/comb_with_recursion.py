def comb (arr, r):
    result = []
    if r == 1:
        return [[i] for i in arr]
    
    for i in range(len(arr)):
        elem = arr[i]
        print(elem)
        for rest in comb(arr[i+1:], r-1):
            print(rest)
            result.append([elem] + rest)

    return result 


print(comb([1,2,3,4],3))
# print(comb([1,2], 3))


# lst = [1,2,3]
# print(lst.append([]))
# print(lst + [])