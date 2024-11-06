# Function to perform partition (deterministic)
def partition(arr, low, high):
    # Taking the last element as the pivot
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1

            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Quick Sort function using deterministic partition
def quick_sort_deterministic(arr, low, high):
    if low < high:
        # Find the pivot position
        pi = partition(arr, low, high)

        # Sort elements before the pivot
        quick_sort_deterministic(arr, low, pi - 1)

        # Sort elements after the pivot
        quick_sort_deterministic(arr, pi + 1, high)


# Main function to run the program
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    arr = []
    print()

    # Input the elements of the array
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    print("Original array:\n", arr)

    # Perform deterministic quicksort
    quick_sort_deterministic(arr, 0, n - 1)

    # Output the sorted array
    print("\nSorted array using Deterministic approach:\n", arr)
