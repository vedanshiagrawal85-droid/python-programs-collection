def factorial_iterative(n: int) -> int:
    """Calculates factorial using an iterative approach."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    """Calculates factorial using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    test_values = [0, 1, 5, 7, 10]
    print("--- Factorial Calculation ---")
    for val in test_values:
        print(f"Factorial of {val}: {factorial_iterative(val)} (Iterative) == {factorial_recursive(val)} (Recursive)")
