class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


# Function to calculate the maximum value for fractional knapsack
def fractional_knapsack(capacity, items):
    # Sort items by value-to-weight ratio in descending order
    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0.0
    for item in items:
        if capacity - item.weight >= 0:
            # Take the whole item
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fraction of the remaining item
            total_value += item.value * (capacity / item.weight)
            break

    return total_value


# Main program
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    capacity = int(input("Enter the knapsack capacity: "))

    items = []
    for i in range(n):
        value = int(input(f"Enter value of item {i + 1}: "))
        weight = int(input(f"Enter weight of item {i + 1}: "))
        items.append(Item(value, weight))

    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in Fractional Knapsack: {max_value}")
