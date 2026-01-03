"""
Optimized versions of the inefficient code examples.
This file demonstrates efficient coding practices and performance improvements.
"""

def find_duplicates_fast(numbers):
    """
    OPTIMIZED: O(n) time complexity using a set.
    Tracks seen numbers and duplicates in a single pass.
    Performance gain: ~100x faster for large lists.
    """
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)


def process_data_fast(data):
    """
    OPTIMIZED: Single pass using generator expression and built-in sum.
    Combines filter, map, and reduce operations efficiently.
    Performance gain: ~3x faster, more memory efficient.
    """
    return sum(item ** 2 for item in data if item > 0)


def string_concatenation_fast(items):
    """
    OPTIMIZED: Using join() which is O(n) instead of O(n²).
    join() pre-allocates memory for the result.
    Performance gain: ~10x faster for large lists.
    """
    return ",".join(str(item) for item in items)


def search_in_set_fast(target, data_set):
    """
    OPTIMIZED: Using a set for O(1) average lookup time.
    For repeated searches, convert list to set once.
    Performance gain: ~100x faster for large datasets.
    """
    return target in data_set


def calculate_fibonacci_fast(n, memo=None):
    """
    OPTIMIZED: Memoization reduces time complexity to O(n).
    Caches previously calculated values.
    Performance gain: Exponential improvement for large n.
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = calculate_fibonacci_fast(n - 1, memo) + calculate_fibonacci_fast(n - 2, memo)
    return memo[n]


def calculate_fibonacci_iterative(n):
    """
    OPTIMIZED: Iterative approach with O(n) time and O(1) space.
    Even better than memoization for space efficiency.
    """
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


# Global cache for configuration
_config_cache = None

def load_config_cached():
    """
    OPTIMIZED: Load configuration once and cache it.
    Subsequent calls return cached value.
    Performance gain: File I/O eliminated after first call.
    
    Note: This is example code for demonstration purposes.
    In production, add proper error handling and path validation.
    """
    global _config_cache
    if _config_cache is None:
        try:
            with open('config.txt', 'r') as f:
                _config_cache = f.read()
        except FileNotFoundError:
            _config_cache = ""  # Return default for demonstration
    return _config_cache


def check_membership_fast(items, search_list):
    """
    OPTIMIZED: Convert to set once before the loop.
    Reduces time complexity from O(n*m) to O(n+m).
    Performance gain: ~100x faster for large lists.
    """
    search_set = set(search_list)
    return [item for item in items if item in search_set]


class DatabaseConnectionPool:
    """
    OPTIMIZED: Connection pooling to reuse database connections.
    Maintains a pool of connections instead of creating new ones.
    Performance gain: ~10x faster for multiple queries.
    
    Note: This is example/pseudocode for demonstration purposes.
    The connection object is a placeholder and not meant to be executed.
    In real implementations, use libraries like SQLAlchemy or connection pool libraries.
    """
    def __init__(self, pool_size=5):
        self.pool = [self.create_connection() for _ in range(pool_size)]
        self.available = list(self.pool)
    
    def query(self, sql):
        # Get connection from pool
        connection = self.get_connection()
        try:
            result = connection.execute(sql)
            return result
        finally:
            # Return connection to pool
            self.release_connection(connection)
    
    def get_connection(self):
        if self.available:
            return self.available.pop()
        # If no connections available, wait or create new one
        return self.create_connection()
    
    def release_connection(self, connection):
        self.available.append(connection)
    
    def create_connection(self):
        """
        Placeholder for connection creation.
        In real code, this would return an actual database connection object.
        """
        pass


def copy_list_efficiently(original_list):
    """
    OPTIMIZED: Use built-in list copying methods.
    list.copy() or slicing [:] are implemented in C and much faster.
    Performance gain: ~2x faster.
    """
    return original_list.copy()  # or original_list[:]


def batch_process_data(data, batch_size=1000):
    """
    OPTIMIZED: Process data in batches to reduce memory usage.
    Useful for large datasets that don't fit in memory.
    """
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        yield batch  # Process batch lazily


def use_list_comprehension(data):
    """
    OPTIMIZED: List comprehensions are faster than loops.
    They're implemented in C and optimize better.
    Performance gain: ~1.5-2x faster than regular loops.
    """
    # Instead of:
    # result = []
    # for item in data:
    #     if item > 0:
    #         result.append(item * 2)
    
    return [item * 2 for item in data if item > 0]
