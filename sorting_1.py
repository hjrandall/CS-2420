import random
import math
import sys
class Compare:
    def __init__(self):
        self.compares=0
    
def bubbleSort(list,c):
    changed=True
    while changed:
        changed=False
        for i in range(len(list)-1):
            c.compares+=1
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                changed=True


# def ShakerSort(C, c):
#     Changed = True
#     while Changed is True:
#         Changed = False
#         for i in range(len(C) - 1):
#             c.compares += 1
#             if C[i] > C[i + 1]:
#                 C[i],C[i + 1] = C[i + 1], C[i]
#                 Changed = True
#         for i in range(len(C)-2, -1, -1):
#             c.compares += 1
#             if C[i] > C[i + 1]:
#                 C[i],C[i + 1] = C[i + 1], C[i]
#                 Changed = True
def shakerSort(list,c):
    changed=True
    while changed:
        changed=False
        for i in range(len(list)-1):
            c.compares+=1
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                changed=True
        for i in range(len(list)-2,-1,-1):
            c.compares+=1
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                changed=True
    
def countingSort(list,c):
    c.compares=len(list)
#     container=[0]*len(list)
#     for v in list:
#         container[v]+=1
#     position=0
#     for index in range(len(container)):
#         count=container[index]
#         for j in range(count):
#             list[position]=index
#             position+=1
#     return list
def randomList(list_length):
    list=[]
    for i in range(list_length):
        num= random.randrange(0,list_length-1)
        list.append(num)
    return list

def MergeSort(A, c):
    if len(A)<= 1:
        return
    mid = len(A)//2
    left = A[:mid]
    right = A[mid:]

    MergeSort(left, c)
    MergeSort(right, c)

    left_index = 0
    right_index = 0
    kounter = 0
    while left_index < len(left) and right_index < len(right):
        c.compares += 1
        if left[left_index] <= right[right_index]:
            A[kounter] = left[left_index]
            left_index += 1

        else:
            A[kounter] = right[right_index]
            right_index += 1
    while left_index < len(left):
        A[kounter] = left[left_index]
        left_index += 1
        kounter += 1
    while right_index < len(right):
        A[kounter] = right[right_index]
        right_index += 1
        kounter += 1

# def merge(list,c):
#     # print("hi")
#     if len(list)<=1:
#         return
#     mid=len(list)//2
#     left=list[:mid]
#     right=list[mid:]
#     merge(left,c)
#     merge(right,c)
#     li=0
#     ri=0
#     kount=0
#     while li<len(left)and ri<len(right):
#         c.compares+=1
#         if left[li]<=right[ri]:
#             list[kount]=left[li]
#             li+=1
#         else:
#             list[kount]=right[ri]
#             ri+=1
#         kount+=1
#     while li<len(left):
#         list[kount]=left[li]
#         li+=1
#         kount+=1
#     while ri<len(right):
#         list[kount]=right[ri]
#         ri+=1
#         kount+=1



# def quicky(list,c):
#     quick_sort(list,0,len(list)-1,False,c)

# def mod(list,c):
#     quick_sort(list,0,len(list)-1,True,c)

# def quick_sort(list,low, high,mod,c):
#     if high-low<=0:
#         return
#     if mod:
#         mid=(low+high)//2
#         list[low],list[mid]=list[mid],list[low]
#     pivot=low
#     lmg=low+1
#     for i in range(low+1,high+1):
#         c.compares+=1
#         if list[i]<list[pivot]:
#             list[i],list[lmg]=list[lmg],list[i]
#             lmg+=1
#     pivot=lmg-1
#     list[low],list[pivot]=list[pivot],list[low]
#     quick_sort(list,low ,pivot-1,mod,c)
#     quick_sort(list,pivot+1,high,mod,c)
   
def QuickSort(A, c):
    QuickSortR(A, 0, len(A)- 1, False, c)
    #order = N*LogN or to degenerate N^2

def ModifiedQuickSort(A, c):
    QuickSortR(A, 0, len(A)- 1, True, c)
    #order = N*LogN or less likley to degenerate N^2

def QuickSortR(A, low, high, mod, c):
    if high - low <= 0:
        return
    if mod:
         mid = (low + high)//2
         A[low],A[mid] = A[mid],A[low]
    
    pivot = low
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        c.compares += 1
        if A[i] < A[pivot]:
            A[i],A[lmgt] = A[lmgt],A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[low],A[pivot] = A[pivot],A[low]
    QuickSortR(A, low, pivot - 1, mod, c)
    QuickSortR(A, pivot + 1, high, mod, c)

# def mod_quick_sort(list,low, high):
#     if high-low<=0:
#         return
#     mid=(low+high)//2
#     list[low],list[mid]=list[mid],list[low]
#     pivot=low
#     lmg=low+1
#     for i in range(low+1,high):
#         if list[i]<list[pivot]:
#             list[i],list[lmg]=list[lmg],list[i]
#             lmg+=1
#     pivot=lmg-1
#     list[low],list[pivot]=list[pivot],list[low]
#     quick_sort(list,0 ,pivot-1)
#     quick_sort(list,pivot+1,high)
#     return list
def math_log(num):
    if num!=0:
        num=math.log(num)/math.log(2)
    return num
def main():
    sys.setrecursionlimit(5000)
    sorts=["mod","merge","quicky","count","bubble","shake"]
    sorts2=[ModifiedQuickSort,MergeSort,QuickSort,countingSort,bubbleSort,shakerSort]
    print(end="      ")
    for sort in sorts:
        print (sort,end="  ")
    print()
    for s in range(3,12):
        print("%02d"%s, end="   ")
        size=2**s
        for sort in sorts2:
            a=randomList(size)
            c=Compare()
            sort(a,c)
            print("%05.2f" %math_log(c.compares),end="  ")
            
        print()
def order(a,size):
    a.sort()
    a[0],a[size-1]=a[size-1],a[0]

    return a
def main2():
    sys.setrecursionlimit(5000)
    sorts=["mod","merge","quicky","count","bubble","shake"]
    sorts2=[ModifiedQuickSort,MergeSort,QuickSort,countingSort,bubbleSort,shakerSort]
    print(end="      ")
    for sort in sorts:
        print (sort,end="  ")
    print()
    for s in range(3,12):
        print("%02d"%s, end="   ")
        size=2**s
        for sort in sorts2:
            a=randomList(size)
            kinda_sort=order(a,size)
            c=Compare()
            sort(kinda_sort,c)
            print("%05.2f" %math_log(c.compares),end="  ")
            
        print()

main()
main2()
