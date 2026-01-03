"""
Performance benchmarks comparing inefficient vs optimized code.
Run this script to see the actual performance differences.
"""

import time
import sys
from examples.inefficient_code import (
    find_duplicates_slow,
    process_data_slow,
    string_concatenation_slow,
    calculate_fibonacci_slow,
    check_membership_slow,
)
from examples.optimized_code import (
    find_duplicates_fast,
    process_data_fast,
    string_concatenation_fast,
    calculate_fibonacci_fast,
    calculate_fibonacci_iterative,
    check_membership_fast,
)


def benchmark(func, *args, runs=1):
    """Measure execution time of a function."""
    start = time.time()
    for _ in range(runs):
        result = func(*args)
    end = time.time()
    return end - start, result


def format_time(seconds):
    """Format time in appropriate units."""
    if seconds < 0.001:
        return f"{seconds * 1000000:.2f} μs"
    elif seconds < 1:
        return f"{seconds * 1000:.2f} ms"
    else:
        return f"{seconds:.2f} s"


def print_comparison(name, slow_time, fast_time, improvement):
    """Print a formatted comparison of execution times."""
    print(f"\n{name}")
    print(f"  Inefficient: {format_time(slow_time)}")
    print(f"  Optimized:   {format_time(fast_time)}")
    print(f"  Improvement: {improvement:.1f}x faster")


def main():
    print("=" * 60)
    print("Performance Benchmark: Inefficient vs Optimized Code")
    print("=" * 60)
    
    # Test 1: Find duplicates
    print("\n1. Finding Duplicates")
    test_data = list(range(1000)) + list(range(500))
    
    slow_time, _ = benchmark(find_duplicates_slow, test_data)
    fast_time, _ = benchmark(find_duplicates_fast, test_data)
    improvement = slow_time / fast_time if fast_time > 0 else 0
    print_comparison("Find Duplicates (1500 elements)", slow_time, fast_time, improvement)
    
    # Test 2: Process data
    print("\n2. Processing Data (filter, square, sum)")
    test_data = list(range(-500, 500))
    
    slow_time, slow_result = benchmark(process_data_slow, test_data, runs=100)
    fast_time, fast_result = benchmark(process_data_fast, test_data, runs=100)
    improvement = slow_time / fast_time if fast_time > 0 else 0
    print_comparison("Process 1000 elements (100 runs)", slow_time, fast_time, improvement)
    assert slow_result == fast_result, "Results don't match!"
    
    # Test 3: String concatenation
    print("\n3. String Concatenation")
    test_data = list(range(1000))
    
    slow_time, _ = benchmark(string_concatenation_slow, test_data, runs=10)
    fast_time, _ = benchmark(string_concatenation_fast, test_data, runs=10)
    improvement = slow_time / fast_time if fast_time > 0 else 0
    print_comparison("Concatenate 1000 items (10 runs)", slow_time, fast_time, improvement)
    
    # Test 4: Fibonacci (smaller numbers for slow version)
    print("\n4. Fibonacci Calculation")
    n = 30
    
    slow_time, slow_result = benchmark(calculate_fibonacci_slow, n)
    fast_time, fast_result = benchmark(calculate_fibonacci_fast, n)
    iterative_time, iterative_result = benchmark(calculate_fibonacci_iterative, n)
    
    improvement_memo = slow_time / fast_time if fast_time > 0 else 0
    improvement_iter = slow_time / iterative_time if iterative_time > 0 else 0
    
    print(f"\nFibonacci({n})")
    print(f"  Inefficient (recursive): {format_time(slow_time)}")
    print(f"  Optimized (memoization): {format_time(fast_time)} ({improvement_memo:.1f}x faster)")
    print(f"  Optimized (iterative):   {format_time(iterative_time)} ({improvement_iter:.1f}x faster)")
    assert slow_result == fast_result == iterative_result, "Results don't match!"
    
    # Test 5: Membership checking
    print("\n5. Membership Checking")
    items = list(range(100))
    search_list = list(range(1000))
    
    slow_time, _ = benchmark(check_membership_slow, items, search_list, runs=10)
    fast_time, _ = benchmark(check_membership_fast, items, search_list, runs=10)
    improvement = slow_time / fast_time if fast_time > 0 else 0
    print_comparison("Check 100 items in 1000 elements (10 runs)", slow_time, fast_time, improvement)
    
    print("\n" + "=" * 60)
    print("Benchmark Complete!")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("  • Choose appropriate data structures (sets vs lists)")
    print("  • Minimize iterations and nested loops")
    print("  • Use built-in functions and comprehensions")
    print("  • Cache expensive operations")
    print("  • Consider algorithm complexity (Big O notation)")


if __name__ == "__main__":
    main()
