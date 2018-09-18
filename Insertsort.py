


def InsertSort(SortArray):
    for i in range(1,len(SortArray)):
        Insert(SortArray, i)

def Insert(SortArray, i):
    temp = SortArray[i]
    for LowColumn in range(i - 1, -1, -1):
        if temp < SortArray[LowColumn]:
            SortArray[LowColumn + 1] = SortArray[LowColumn]
        else:
            SortArray[LowColumn + 1] = temp
            break
    else:
        SortArray[0] = temp
            
A = [6,3,8,5,7,1,9]
InsertSort(A)
print(A)