'''Researching Merge, Insertion and Timsort algorythms'''

import timeit
import random

def merge_sort(arr):
    '''
    Merge sort algorythm
    '''
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    '''
    Insertion sort algorythm
    '''
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Test Data
test_data_small = random.sample(range(100), 10)
test_data_medium = random.sample(range(1000), 100)
test_data_large = random.sample(range(10000), 1000)

# Timeit

merge_sort_time_small = timeit.timeit(lambda: merge_sort(test_data_small.copy()), number=1000)
insertion_sort_time_small = timeit.timeit(lambda: insertion_sort(test_data_small.copy()), number=1000)
timsort_time_small = timeit.timeit(lambda: sorted(test_data_small.copy()), number=1000)

merge_sort_time_medium = timeit.timeit(lambda: merge_sort(test_data_medium.copy()), number=100)
insertion_sort_time_medium = timeit.timeit(lambda: insertion_sort(test_data_medium.copy()), number=100)
timsort_time_medium = timeit.timeit(lambda: sorted(test_data_medium.copy()), number=100)

merge_sort_time_large = timeit.timeit(lambda: merge_sort(test_data_large.copy()), number=10)
insertion_sort_time_large = timeit.timeit(lambda: insertion_sort(test_data_large.copy()), number=10)
timsort_time_large = timeit.timeit(lambda: sorted(test_data_large.copy()), number=10)

print("Small Dataset:")
print("Merge Sort Time:", merge_sort_time_small)
print("Insertion Sort Time:", insertion_sort_time_small)
print("Timsort Time:", timsort_time_small)

print("\nMedium Dataset:")
print("Merge Sort Time:", merge_sort_time_medium)
print("Insertion Sort Time:", insertion_sort_time_medium)
print("Timsort Time:", timsort_time_medium)

print("\nLarge Dataset:")
print("Merge Sort Time:", merge_sort_time_large)
print("Insertion Sort Time:", insertion_sort_time_large)
print("Timsort Time:", timsort_time_large)

print('''
    Цей код вимірює час виконання для кожного алгоритму сортування на трьох різних наборах даних: невеликому, середньому і великому. В якості невеликого набору даних використовуються 10 випадкових чисел з діапазону 0-99, як середній - 100 випадкових чисел з діапазону 0-999, а як великий - 1000 випадкових чисел з діапазону 0-9999.

    Після запуску цього коду можна порівняти час виконання кожного алгоритму на різних наборах даних. Час виконання сортування злиттям та сортування вставками зазвичай збільшується значно швидше, ніж у Timsort. Тим не менш, Timsort зазвичай виявляється набагато швидшим для середніх і великих наборів даних, завдяки його комбінованому підходу, який використовує сортування злиттям і сортування вставками, що дозволяє йому бути більш ефективним для різноманітних типів даних та розмірів масивів. Це підтверджує теоретичні припущення щодо продуктивності Timsort порівняно з іншими алгоритмами сортування.

    Отже, з цього експерименту можна зробити висновок, що Timsort дійсно ефективний алгоритм сортування, особливо для великих наборів даних, і це пояснює, чому програмісти зазвичай віддають перевагу використанню вбудованих алгоритмів сортування Python, таких як sorted(), замість того, щоб самостійно реалізовувати алгоритми сортування.
''')
