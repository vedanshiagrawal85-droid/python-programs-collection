from typing import List

def fibonacci_iterative(n_terms: int) -> List[int]:
    """Generates the Fibonacci series up to n terms."""
    if n_terms <= 0:
        return []
    if n_terms == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n_terms:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def fibonacci_nth_memo(n: int, memo: dict = None) -> int:
    """Returns the nth Fibonacci number using memoization."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci_nth_memo(n - 1, memo) + fibonacci_nth_memo(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    n = 10
    print(f"First {n} Fibonacci numbers: {fibonacci_iterative(n)}")
    print(f"10th Fibonacci number: {fibonacci_nth_memo(10)}")
