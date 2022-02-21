- 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인
- 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색 (log시간)
           -> 시작점, 끝점, 중간점을 이용하여 탐색범위를 설정

- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산횟수 : logN => 시간복잡도:O(logN)

- 이진 탐색 구현(재귀함수)

```python
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

n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
```
