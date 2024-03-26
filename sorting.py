import random
import time
import matplotlib
import matplotlib.pyplot as plt

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

def checkBubbleSort(size):
    random_list_for_slow = [random.randint(0, 1000) for _ in range(size)]
    start_time = time.time()
    bubble_sort(random_list_for_slow)
    end_time = time.time()
    print("Сортировка пузырьком: ", end_time - start_time)
    return end_time - start_time

def checkSelectionSort(size):
    random_list_for_slow = [random.randint(0, 1000) for _ in range(size)]
    start_time = time.time()
    selection_sort(random_list_for_slow)
    end_time = time.time()
    print("Сортировка выбором: ", end_time - start_time)
    return end_time - start_time

def checkInserionSort(size):
    random_list_for_slow = [random.randint(0, 1000) for _ in range(size)]
    start_time = time.time()
    insertion_sort(random_list_for_slow)
    end_time = time.time()
    print("Сортировка вставками: ", end_time - start_time)
    return end_time - start_time

def checkHeapSort(size):
    random_list_for_fast = [random.randint(0, 1000) for _ in range(size)]
    start_time = time.time()
    heap_sort(random_list_for_fast)
    end_time = time.time()
    print("Пирамидаидальная сортировка: ", end_time - start_time)
    return end_time - start_time

def checkMergeSort(size):
    random_list_for_fast = [random.randint(0, 1000) for _ in range(size)]
    start_time = time.time()
    random_list_for_fast = merge_sort(random_list_for_fast)
    end_time = time.time()
    print("Сортировка слиянием: ", end_time - start_time)
    return end_time - start_time

def checkQuickSort(size):
    random_list_for_fast = [random.randint(0, 1000) for _ in range(size)]
    start_time = time.time()
    quick_sort(random_list_for_fast)
    end_time = time.time()
    print("Быстрая сортировка: ", end_time - start_time)
    return end_time - start_time


# Verify it works  10000 20000 50 000 70 000 100 000

sizes = [100, 1000, 3000, 5000]
arrForPlotBuble = (checkBubbleSort(100), checkBubbleSort(1000), checkBubbleSort(3000), checkBubbleSort(5000))
arrForPlotSel = (checkSelectionSort(100), checkSelectionSort(1000), checkSelectionSort(3000), checkSelectionSort(5000))
arrForPlotIns = (checkInserionSort(100), checkInserionSort(1000), checkInserionSort(3000), checkInserionSort(5000))
plt.plot(sizes, arrForPlotBuble, label='Сортировка пузырьком')
plt.plot(sizes, arrForPlotSel, label='Сортировка выбором')
plt.plot(sizes, arrForPlotIns, label='Сортировка вставками')
plt.xlabel('Размер входных данных')
plt.ylabel('Время выполнения (секунды)')
plt.title('Сравнение времени выполнения алгоритмов сортировки')
plt.legend()
plt.grid(True)
plt.show()

sizes = [10000, 20000, 50000, 100000]
arrForPlotHeap = (checkHeapSort(10000), checkHeapSort(20000), checkHeapSort(50000), checkHeapSort(100000))
arrForPlotMerge = (checkMergeSort(10000), checkMergeSort(20000), checkMergeSort(50000), checkMergeSort(100000))
arrForPlotQuick = (checkQuickSort(10000), checkQuickSort(20000), checkQuickSort(50000), checkQuickSort(100000))
plt.plot(sizes, arrForPlotHeap, label='Пирамидаидальная сортировка')
plt.plot(sizes, arrForPlotMerge, label='Сортировка слиянием')
plt.plot(sizes, arrForPlotQuick, label='Быстрая сортировка')
plt.xlabel('Размер входных данных')
plt.ylabel('Время выполнения (секунды)')
plt.title('Сравнение времени выполнения алгоритмов сортировки')
plt.legend()
plt.grid(True)
plt.show()
