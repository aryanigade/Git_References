import random


# Function to perform partition with random pivot
def partition_random(arr, low, high):
    # Select a random pivot index between low and high
    rand_pivot = random.randint(low, high)

    # Swap random pivot with the last element
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the index of the pivot
    return i + 1


# Quick Sort function using randomized partition
def quick_sort_randomized(arr, low, high):
    if low < high:
        # Find the pivot position using random pivot
        pi = partition_random(arr, low, high)

        # Sort elements before the pivot
        quick_sort_randomized(arr, low, pi - 1)

        # Sort elements after the pivot
        quick_sort_randomized(arr, pi + 1, high)


# Main function to run the program
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    arr = []
    print()

    # Input the elements of the array
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    print("Original array:\n", arr)

    # Perform randomized quicksort
    quick_sort_randomized(arr, 0, n - 1)

    # Output the sorted array
    print("\nSorted array using Randomized approach:\n", arr)
