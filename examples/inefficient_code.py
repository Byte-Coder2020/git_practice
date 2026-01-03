"""
Example of inefficient code with common performance anti-patterns.
This file demonstrates slow and inefficient coding practices.
"""

def find_duplicates_slow(numbers):
    """
    INEFFICIENT: O(n²) time complexity using nested loops.
    For large lists, this becomes extremely slow.
    """
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])
    return duplicates


def process_data_slow(data):
    """
    INEFFICIENT: Multiple iterations over the same list.
    Each operation scans the entire list separately.
    """
    # First pass: filter
    filtered = []
    for item in data:
        if item > 0:
            filtered.append(item)
    
    # Second pass: square
    squared = []
    for item in filtered:
        squared.append(item ** 2)
    
    # Third pass: sum
    total = 0
    for item in squared:
        total += item
    
    return total


def string_concatenation_slow(items):
    """
    INEFFICIENT: String concatenation in a loop creates new string objects
    repeatedly, leading to O(n²) time complexity.
    """
    result = ""
    for item in items:
        result += str(item) + ","
    return result[:-1] if result else ""


def search_in_list_slow(target, data):
    """
    INEFFICIENT: Linear search O(n) when using a list.
    For repeated searches, this is very slow.
    """
    return target in data


def calculate_fibonacci_slow(n):
    """
    INEFFICIENT: Recursive implementation without memoization.
    Has exponential time complexity O(2^n).
    """
    if n <= 1:
        return n
    return calculate_fibonacci_slow(n - 1) + calculate_fibonacci_slow(n - 2)


def load_config_repeatedly():
    """
    INEFFICIENT: Re-reading file on every function call.
    File I/O is expensive and should be cached when possible.
    
    Note: This is example code for demonstration purposes.
    In production, add proper error handling and path validation.
    """
    try:
        with open('config.txt', 'r') as f:
            config = f.read()
        return config
    except FileNotFoundError:
        return ""  # Return default for demonstration


def check_membership_slow(items, search_list):
    """
    INEFFICIENT: Converting to set inside loop.
    The conversion happens repeatedly for each item.
    """
    results = []
    for item in items:
        if item in set(search_list):
            results.append(item)
    return results


class DatabaseConnection:
    """
    INEFFICIENT: Opening new database connection for each query.
    Connection pooling should be used instead.
    
    Note: This is example/pseudocode for demonstration purposes.
    The connection object is a placeholder and not meant to be executed.
    """
    def query(self, sql):
        # Simulating opening a new connection each time
        connection = self.create_connection()
        result = connection.execute(sql)
        connection.close()
        return result
    
    def create_connection(self):
        """
        Placeholder for connection creation.
        In real code, this would return an actual database connection object.
        """
        pass


def copy_list_inefficiently(original_list):
    """
    INEFFICIENT: Manual copying when built-in methods exist.
    Slower and more error-prone.
    """
    new_list = []
    for item in original_list:
        new_list.append(item)
    return new_list
