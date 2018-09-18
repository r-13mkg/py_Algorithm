
def sort(A):
    for i in range(0, len(A) - 1):
        minAddr = SerchMinValue(A,i)
        if minAddr != -1:
            temp = A[i]
            A[i] = A[minAddr]
            A[minAddr] = temp
            
# 一番小さい数値を返す
def SerchMinValue(A, SortAddr):
    minValue = A[SortAddr]
    minAddr = 0
    for tempValue in range(SortAddr + 1, len(A)):
        if minValue > A[tempValue]:
            minValue = A[tempValue]
            minAddr = tempValue
    if A[SortAddr] <= minValue:
        # 検索対象が一番小さい場合は-1を返却
        return -1
    else:
        return minAddr