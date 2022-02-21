# https://www.acmicpc.net/problem/1920
import sys
input = sys.stdin.readline

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for a in arr2:
    if binary_search(arr1,a,0,n-1) == None:
        print(0)
    else:
        print(1)
