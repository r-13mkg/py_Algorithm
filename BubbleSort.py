
def BubbleSort(SortArry):
    for i in range(0,len(SortArry)-1):
        if ChangeValue(SortArry, i) == 0:
            break


def ChangeValue(SortArry,i):
    ChangeCount = 0
    for remaining in range(len(SortArry)-1,i,-1):
        if SortArry[remaining] < SortArry[remaining -1]:
            temp = SortArry[remaining]
            SortArry[remaining] = SortArry[remaining-1]
            SortArry[remaining - 1] = temp
            ChangeCount = ChangeCount + 1

    return ChangeCount


A = [5,7,2,9,4,1,8,6]

BubbleSort(A)

print(A)