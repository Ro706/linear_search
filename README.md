# linear_search
`Linear search` is a simple search algorithm that searches for an element in a list in sequential order. It is also known as sequential search. In Python, linear searching makes the searching technique quite efficient and easy for any element to be searched. Linear searching in Python is performed in a sequential manner by comparing one element to the next and so on until the required element is found for manipulation and transformation

```
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
x = 30

result = linear_search(arr, x)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)
```
