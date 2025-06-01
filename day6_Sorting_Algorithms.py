def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

# Collecting user input
user_input = input("Enter numbers separated by commas (e.g., 1, 2, 3): ")
user_list = [int(num.strip()) for num in user_input.split(",")]

# Make copies of the list for each sort
bubble_sorted = bubble_sort(user_list.copy())
selection_sorted = selection_sort(user_list.copy())

print("Original list:", user_list)
print("Bubble sorted list:", bubble_sorted)
print("Selection sorted list:", selection_sorted)