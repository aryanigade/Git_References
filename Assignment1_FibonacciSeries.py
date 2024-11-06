class Fibonacci:
    def __init__(self):
        self.step_count_recursive = 0
        self.step_count_iterative = 0

    def recursive_fibonacci(self, n):
        # Increment step count each time this function is called
        self.step_count_recursive += 1
        if n <= 1:
            return n
        else:
            return self.recursive_fibonacci(n - 1) + self.recursive_fibonacci(n - 2)

    def iterative_fibonacci(self, n):
        # Reset step count for iterative method
        self.step_count_iterative = 0

        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            self.step_count_iterative += 1  # Increment step count with each iteration
            a, b = b, a + b
        return b

    def display_fibonacci(self, n, method='iterative'):
        if method == 'recursive':
            self.step_count_recursive = 0  # Reset step count for recursive method
            print("Fibonacci series using recursion:")
            for i in range(n):
                print(self.recursive_fibonacci(i), end=" ")
            print(f"\nStep count (recursive): {self.step_count_recursive}")

        elif method == 'iterative':
            print("Fibonacci series using iteration:")
            for i in range(n):
                print(self.iterative_fibonacci(i), end=" ")
            print(f"\nStep count (iterative): {self.step_count_iterative}")
        else:
            print("Invalid method selected.")


# Main program
if __name__ == "__main__":
    fib = Fibonacci()
    n = int(input("Enter the number of terms: "))

    while True:
        print("\nMenu:")
        print("1. Calculate Fibonacci series using recursion")
        print("2. Calculate Fibonacci series using iteration")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            fib.display_fibonacci(n, method='recursive')
        elif choice == 2:
            fib.display_fibonacci(n, method='iterative')
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
