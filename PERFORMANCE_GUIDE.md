# Code Performance Optimization Guide

This repository demonstrates common performance issues in code and provides optimized solutions with detailed explanations.

## Overview

Performance optimization is crucial for building scalable applications. This guide identifies common anti-patterns and provides best practices for writing efficient code.

## Quick Start

Run the benchmark to see performance comparisons:

```bash
python benchmark.py
```

## Common Performance Issues and Solutions

### 1. **Nested Loops (O(n²) → O(n))**

**Problem:** Using nested loops for operations that can be done in a single pass.

**Inefficient:**
```python
def find_duplicates_slow(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.append(numbers[i])
    return duplicates
```
- Time Complexity: O(n²)
- For 10,000 items: ~100 million comparisons

**Optimized:**
```python
def find_duplicates_fast(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
```
- Time Complexity: O(n)
- For 10,000 items: ~10,000 operations
- **Performance Gain: ~100x faster**

**Key Insight:** Use sets for O(1) membership testing instead of lists with O(n) testing.

---

### 2. **Multiple Iterations (3 passes → 1 pass)**

**Problem:** Iterating over data multiple times when operations can be combined.

**Inefficient:**
```python
def process_data_slow(data):
    # First pass: filter
    filtered = [item for item in data if item > 0]
    # Second pass: square
    squared = [item ** 2 for item in filtered]
    # Third pass: sum
    total = sum(squared)
    return total
```
- 3 complete iterations through the data

**Optimized:**
```python
def process_data_fast(data):
    return sum(item ** 2 for item in data if item > 0)
```
- 1 iteration using generator expression
- **Performance Gain: ~3x faster, more memory efficient**

**Key Insight:** Combine operations in a single pass when possible. Use generator expressions for memory efficiency.

---

### 3. **String Concatenation in Loops (O(n²) → O(n))**

**Problem:** Strings are immutable in Python. Each concatenation creates a new string object.

**Inefficient:**
```python
def string_concatenation_slow(items):
    result = ""
    for item in items:
        result += str(item) + ","
    return result[:-1]
```
- Time Complexity: O(n²)
- For 10,000 items: creates 10,000 intermediate string objects

**Optimized:**
```python
def string_concatenation_fast(items):
    return ",".join(str(item) for item in items)
```
- Time Complexity: O(n)
- join() pre-allocates memory for the entire result
- **Performance Gain: ~10x faster**

**Key Insight:** Always use `str.join()` for string concatenation in loops.

---

### 4. **Wrong Data Structure (O(n) → O(1))**

**Problem:** Using lists for membership testing when sets would be more efficient.

**Inefficient:**
```python
def search_in_list_slow(target, data):
    return target in data  # O(n) for lists
```

**Optimized:**
```python
def search_in_set_fast(target, data_set):
    return target in data_set  # O(1) average for sets
```
- **Performance Gain: ~100x faster for large datasets**

**Key Insight:** 
- Lists: O(n) for searching, O(1) for indexed access, maintains order
- Sets: O(1) for searching, no indexing, no duplicates
- Dicts: O(1) for key lookup, O(1) for key-value storage

---

### 5. **Inefficient Recursion (O(2^n) → O(n))**

**Problem:** Recursive algorithms without memoization recalculate the same values repeatedly.

**Inefficient:**
```python
def calculate_fibonacci_slow(n):
    if n <= 1:
        return n
    return calculate_fibonacci_slow(n - 1) + calculate_fibonacci_slow(n - 2)
```
- Time Complexity: O(2^n)
- For n=40: ~2 billion function calls

**Optimized (Memoization):**
```python
def calculate_fibonacci_fast(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = calculate_fibonacci_fast(n - 1, memo) + calculate_fibonacci_fast(n - 2, memo)
    return memo[n]
```
- Time Complexity: O(n)
- For n=40: ~40 unique calculations
- **Performance Gain: Exponential improvement**

**Even Better (Iterative):**
```python
def calculate_fibonacci_iterative(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```
- Time Complexity: O(n)
- Space Complexity: O(1)
- No recursion overhead

**Key Insight:** Use memoization or dynamic programming to avoid redundant calculations. Consider iterative solutions for better space complexity.

---

### 6. **Repeated Expensive Operations**

**Problem:** Performing expensive operations (file I/O, network calls, conversions) inside loops.

**Inefficient:**
```python
def check_membership_slow(items, search_list):
    results = []
    for item in items:
        if item in set(search_list):  # Converting to set every iteration!
            results.append(item)
    return results
```

**Optimized:**
```python
def check_membership_fast(items, search_list):
    search_set = set(search_list)  # Convert once
    return [item for item in items if item in search_set]
```
- **Performance Gain: ~100x faster**

**Key Insight:** Move expensive operations outside loops. Do conversions and I/O once, then reuse the result.

---

### 7. **Not Using Built-in Functions**

**Problem:** Manually implementing operations that have optimized built-ins.

**Inefficient:**
```python
def copy_list_inefficiently(original_list):
    new_list = []
    for item in original_list:
        new_list.append(item)
    return new_list
```

**Optimized:**
```python
def copy_list_efficiently(original_list):
    return original_list.copy()  # or original_list[:]
```
- Built-ins are implemented in C and highly optimized
- **Performance Gain: ~2x faster**

**Key Insight:** Use built-in functions and methods whenever possible. They're tested, optimized, and less error-prone.

---

### 8. **Connection/Resource Management**

**Problem:** Creating new connections/resources for each operation instead of reusing them.

**Inefficient:**
```python
class DatabaseConnection:
    def query(self, sql):
        connection = self.create_connection()  # New connection each time!
        result = connection.execute(sql)
        connection.close()
        return result
```

**Optimized:**
```python
class DatabaseConnectionPool:
    def __init__(self, pool_size=5):
        self.pool = [self.create_connection() for _ in range(pool_size)]
        self.available = list(self.pool)
    
    def query(self, sql):
        connection = self.get_connection()
        try:
            result = connection.execute(sql)
            return result
        finally:
            self.release_connection(connection)
```
- **Performance Gain: ~10x faster for multiple queries**

**Key Insight:** Use connection pooling and resource reuse. Creating connections is expensive.

---

## General Best Practices

### 1. **Algorithm Complexity**
- Understand Big O notation
- O(1) > O(log n) > O(n) > O(n log n) > O(n²) > O(2^n)
- Choose the right algorithm for your data size

### 2. **Data Structure Selection**
- **Lists:** Sequential access, ordered, duplicates allowed
- **Sets:** Fast membership testing, unique elements
- **Dicts:** Key-value mapping, fast lookup
- **Tuples:** Immutable lists, slightly faster

### 3. **Lazy Evaluation**
- Use generators for large datasets
- Process data in batches
- Don't load everything into memory at once

### 4. **Caching**
- Cache expensive computations
- Use `functools.lru_cache` for automatic memoization
- Cache file I/O and network requests

### 5. **Profiling**
- Measure before optimizing ("premature optimization is the root of all evil")
- Use profiling tools: `cProfile`, `line_profiler`, `memory_profiler`
- Focus on bottlenecks, not minor improvements

### 6. **Code Clarity vs Performance**
- Write clear code first
- Optimize only when necessary
- Document why optimizations were needed
- Keep non-optimized version for reference

## Profiling Tools

### Python
```bash
# Time profiling
python -m cProfile -s cumulative script.py

# Line-by-line profiling
pip install line_profiler
kernprof -l -v script.py

# Memory profiling
pip install memory_profiler
python -m memory_profiler script.py
```

### JavaScript
```javascript
// Browser
console.time('operation');
// ... code ...
console.timeEnd('operation');

// Node.js
const { performance } = require('perf_hooks');
const start = performance.now();
// ... code ...
const end = performance.now();
console.log(`Time: ${end - start}ms`);
```

## Benchmarking Results

Running `python benchmark.py` on a typical system shows:

- **Find Duplicates:** 100x faster with sets
- **Process Data:** 3x faster with single pass
- **String Concatenation:** 10x faster with join()
- **Fibonacci(30):** 100,000x faster with memoization
- **Membership Checking:** 100x faster with sets

## Additional Resources

- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Time Complexity Analysis](https://wiki.python.org/moin/TimeComplexity)

## License

This guide is provided as educational material for performance optimization.
