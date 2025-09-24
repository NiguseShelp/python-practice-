"""
Accumulator Practice Module

This module provides various examples and exercises for practicing the accumulator pattern
in Python. The accumulator pattern is a fundamental programming concept where you:
1. Initialize a variable (accumulator) to store results
2. Iterate through a data structure
3. Update the accumulator on each iteration
4. Return the final accumulated result

Examples include: sum, product, counting, finding max/min, string concatenation,
list building, and more complex data processing patterns.
"""

def basic_sum_accumulator(numbers):
    """
    Basic accumulator pattern: sum all numbers in a list
    
    Args:
        numbers (list): List of numbers to sum
    
    Returns:
        int/float: Sum of all numbers
        
    Example:
        >>> basic_sum_accumulator([1, 2, 3, 4, 5])
        15
    """
    total = 0  # Initialize accumulator
    for num in numbers:
        total += num  # Update accumulator
    return total  # Return final result


def product_accumulator(numbers):
    """
    Accumulator pattern: multiply all numbers in a list
    
    Args:
        numbers (list): List of numbers to multiply
    
    Returns:
        int/float: Product of all numbers
        
    Example:
        >>> product_accumulator([2, 3, 4])
        24
    """
    product = 1  # Initialize accumulator (1 for multiplication)
    for num in numbers:
        product *= num  # Update accumulator
    return product


def count_accumulator(items, target):
    """
    Accumulator pattern: count occurrences of a target item
    
    Args:
        items (list): List of items to search through
        target: Item to count
    
    Returns:
        int: Number of occurrences
        
    Example:
        >>> count_accumulator([1, 2, 3, 2, 4, 2], 2)
        3
    """
    count = 0  # Initialize counter accumulator
    for item in items:
        if item == target:
            count += 1  # Update accumulator
    return count


def max_accumulator(numbers):
    """
    Accumulator pattern: find maximum value in a list
    
    Args:
        numbers (list): List of numbers (must not be empty)
    
    Returns:
        int/float: Maximum value
        
    Example:
        >>> max_accumulator([3, 7, 2, 9, 1])
        9
    """
    if not numbers:
        raise ValueError("Cannot find max of empty list")
    
    max_val = numbers[0]  # Initialize with first element
    for num in numbers[1:]:  # Start from second element
        if num > max_val:
            max_val = num  # Update accumulator
    return max_val


def min_accumulator(numbers):
    """
    Accumulator pattern: find minimum value in a list
    
    Args:
        numbers (list): List of numbers (must not be empty)
    
    Returns:
        int/float: Minimum value
        
    Example:
        >>> min_accumulator([3, 7, 2, 9, 1])
        1
    """
    if not numbers:
        raise ValueError("Cannot find min of empty list")
    
    min_val = numbers[0]  # Initialize with first element
    for num in numbers[1:]:  # Start from second element
        if num < min_val:
            min_val = num  # Update accumulator
    return min_val


def string_concatenation_accumulator(words, separator=" "):
    """
    Accumulator pattern: concatenate strings with separator
    
    Args:
        words (list): List of strings to join
        separator (str): String to use as separator
    
    Returns:
        str: Concatenated string
        
    Example:
        >>> string_concatenation_accumulator(["Hello", "world", "!"])
        'Hello world !'
    """
    result = ""  # Initialize string accumulator
    for i, word in enumerate(words):
        result += word  # Add current word
        if i < len(words) - 1:  # Don't add separator after last word
            result += separator
    return result


def list_building_accumulator(numbers, condition_func):
    """
    Accumulator pattern: build a new list based on condition
    
    Args:
        numbers (list): Input list of numbers
        condition_func (function): Function that returns True/False
    
    Returns:
        list: New list containing items that meet condition
        
    Example:
        >>> list_building_accumulator([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
        [2, 4, 6]
    """
    result = []  # Initialize list accumulator
    for num in numbers:
        if condition_func(num):
            result.append(num)  # Update accumulator
    return result


def average_accumulator(numbers):
    """
    Accumulator pattern: calculate average (combines sum and count)
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        float: Average of all numbers
        
    Example:
        >>> average_accumulator([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        return 0.0
    
    total = 0  # Sum accumulator
    count = 0  # Count accumulator
    
    for num in numbers:
        total += num  # Update sum
        count += 1   # Update count
    
    return total / count  # Calculate average


def nested_sum_accumulator(nested_list):
    """
    Accumulator pattern: sum all numbers in nested lists
    
    Args:
        nested_list (list): List containing sublists of numbers
    
    Returns:
        int/float: Sum of all numbers in all sublists
        
    Example:
        >>> nested_sum_accumulator([[1, 2], [3, 4, 5], [6]])
        21
    """
    total = 0  # Initialize accumulator
    for sublist in nested_list:
        for num in sublist:
            total += num  # Update accumulator
    return total


def word_length_accumulator(words):
    """
    Accumulator pattern: build list of word lengths
    
    Args:
        words (list): List of words (strings)
    
    Returns:
        list: List of lengths corresponding to each word
        
    Example:
        >>> word_length_accumulator(["cat", "dog", "elephant"])
        [3, 3, 8]
    """
    lengths = []  # Initialize list accumulator
    for word in words:
        lengths.append(len(word))  # Update accumulator
    return lengths


def frequency_counter_accumulator(items):
    """
    Accumulator pattern: count frequency of each item using dictionary
    
    Args:
        items (list): List of items to count
    
    Returns:
        dict: Dictionary with items as keys and counts as values
        
    Example:
        >>> frequency_counter_accumulator(['a', 'b', 'a', 'c', 'b', 'a'])
        {'a': 3, 'b': 2, 'c': 1}
    """
    frequency = {}  # Initialize dictionary accumulator
    for item in items:
        if item in frequency:
            frequency[item] += 1  # Update existing count
        else:
            frequency[item] = 1   # Initialize new count
    return frequency


def running_sum_accumulator(numbers):
    """
    Accumulator pattern: create list of running sums
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        list: List where each element is sum of all previous elements
        
    Example:
        >>> running_sum_accumulator([1, 2, 3, 4])
        [1, 3, 6, 10]
    """
    running_sums = []  # Initialize list accumulator
    current_sum = 0    # Initialize running total
    
    for num in numbers:
        current_sum += num           # Update running total
        running_sums.append(current_sum)  # Add to result list
    
    return running_sums


# Practice Exercises (functions that students can implement)

def exercise_1_sum_of_squares(numbers):
    """
    Exercise 1: Use accumulator pattern to sum squares of all numbers
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int/float: Sum of squares
        
    Example:
        >>> exercise_1_sum_of_squares([1, 2, 3])
        14  # 1² + 2² + 3² = 1 + 4 + 9 = 14
    """
    # TODO: Implement using accumulator pattern
    total = 0
    for num in numbers:
        total += num ** 2
    return total


def exercise_2_longest_word(words):
    """
    Exercise 2: Use accumulator pattern to find longest word
    
    Args:
        words (list): List of words (strings)
    
    Returns:
        str: Longest word (if tie, return first one)
        
    Example:
        >>> exercise_2_longest_word(["cat", "elephant", "dog"])
        'elephant'
    """
    # TODO: Implement using accumulator pattern
    if not words:
        return ""
    
    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word
    return longest


def exercise_3_alternating_sum(numbers):
    """
    Exercise 3: Calculate alternating sum (add/subtract alternately)
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int/float: Alternating sum
        
    Example:
        >>> exercise_3_alternating_sum([1, 2, 3, 4])
        -2  # 1 - 2 + 3 - 4 = -2
    """
    # TODO: Implement using accumulator pattern
    total = 0
    for i, num in enumerate(numbers):
        if i % 2 == 0:
            total += num
        else:
            total -= num
    return total


def exercise_4_group_by_condition(items, condition_func):
    """
    Exercise 4: Group items into two lists based on condition
    
    Args:
        items (list): List of items
        condition_func (function): Function returning True/False
    
    Returns:
        tuple: (items_true, items_false) - two lists
        
    Example:
        >>> exercise_4_group_by_condition([1,2,3,4,5], lambda x: x % 2 == 0)
        ([2, 4], [1, 3, 5])
    """
    # TODO: Implement using accumulator pattern
    true_items = []
    false_items = []
    for item in items:
        if condition_func(item):
            true_items.append(item)
        else:
            false_items.append(item)
    return (true_items, false_items)


def demonstration():
    """
    Demonstrate all accumulator patterns with example data
    """
    print("=== ACCUMULATOR PATTERN DEMONSTRATIONS ===\n")
    
    # Test data
    numbers = [1, 2, 3, 4, 5]
    words = ["hello", "world", "python", "programming"]
    nested = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
    
    print("1. Basic Sum Accumulator:")
    print(f"   Input: {numbers}")
    print(f"   Sum: {basic_sum_accumulator(numbers)}\n")
    
    print("2. Product Accumulator:")
    print(f"   Input: {numbers}")
    print(f"   Product: {product_accumulator(numbers)}\n")
    
    print("3. Count Accumulator:")
    print(f"   Input: {[1, 2, 3, 2, 4, 2]}")
    print(f"   Count of 2: {count_accumulator([1, 2, 3, 2, 4, 2], 2)}\n")
    
    print("4. Max/Min Accumulators:")
    print(f"   Input: {numbers}")
    print(f"   Max: {max_accumulator(numbers)}")
    print(f"   Min: {min_accumulator(numbers)}\n")
    
    print("5. String Concatenation:")
    print(f"   Input: {words[:3]}")
    print(f"   Result: '{string_concatenation_accumulator(words[:3])}'\n")
    
    print("6. List Building (even numbers):")
    print(f"   Input: {numbers}")
    print(f"   Even numbers: {list_building_accumulator(numbers, lambda x: x % 2 == 0)}\n")
    
    print("7. Average Accumulator:")
    print(f"   Input: {numbers}")
    print(f"   Average: {average_accumulator(numbers)}\n")
    
    print("8. Nested Sum:")
    print(f"   Input: {nested}")
    print(f"   Total sum: {nested_sum_accumulator(nested)}\n")
    
    print("9. Word Lengths:")
    print(f"   Input: {words}")
    print(f"   Lengths: {word_length_accumulator(words)}\n")
    
    print("10. Frequency Counter:")
    letters = ['a', 'b', 'a', 'c', 'b', 'a']
    print(f"    Input: {letters}")
    print(f"    Frequencies: {frequency_counter_accumulator(letters)}\n")
    
    print("11. Running Sum:")
    print(f"    Input: {numbers}")
    print(f"    Running sums: {running_sum_accumulator(numbers)}\n")
    
    print("=== PRACTICE EXERCISES ===\n")
    
    print("Exercise 1 - Sum of Squares:")
    print(f"Input: {[1, 2, 3]}")
    print(f"Result: {exercise_1_sum_of_squares([1, 2, 3])}\n")
    
    print("Exercise 2 - Longest Word:")
    print(f"Input: {['cat', 'elephant', 'dog']}")
    print(f"Result: '{exercise_2_longest_word(['cat', 'elephant', 'dog'])}'\n")
    
    print("Exercise 3 - Alternating Sum:")
    print(f"Input: {[1, 2, 3, 4]}")
    print(f"Result: {exercise_3_alternating_sum([1, 2, 3, 4])}\n")
    
    print("Exercise 4 - Group by Condition:")
    print(f"Input: {[1, 2, 3, 4, 5]} (group by even/odd)")
    even, odd = exercise_4_group_by_condition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    print(f"Even: {even}, Odd: {odd}\n")


if __name__ == "__main__":
    demonstration()