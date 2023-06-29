class Demo:
    # 冒泡排序
    def bubble_sort(self, arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

