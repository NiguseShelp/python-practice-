"""
Advanced Accumulator Exercises

This module contains more challenging accumulator pattern exercises
that combine multiple concepts and real-world scenarios.
"""

def sales_analysis_accumulator(sales_data):
    """
    Real-world example: Analyze sales data using accumulator patterns
    
    Args:
        sales_data (list): List of dictionaries with 'product', 'price', 'quantity'
    
    Returns:
        dict: Analysis results with total_revenue, total_items, avg_price
        
    Example:
        >>> data = [
        ...     {'product': 'Apple', 'price': 1.0, 'quantity': 10},
        ...     {'product': 'Banana', 'price': 0.5, 'quantity': 20}
        ... ]
        >>> sales_analysis_accumulator(data)
        {'total_revenue': 20.0, 'total_items': 30, 'avg_price': 0.67}
    """
    total_revenue = 0
    total_items = 0
    total_price_sum = 0
    
    for sale in sales_data:
        revenue = sale['price'] * sale['quantity']
        total_revenue += revenue
        total_items += sale['quantity']
        total_price_sum += sale['price']
    
    avg_price = total_price_sum / len(sales_data) if sales_data else 0
    
    return {
        'total_revenue': round(total_revenue, 2),
        'total_items': total_items,
        'avg_price': round(avg_price, 2)
    }


def student_grades_accumulator(student_records):
    """
    Education example: Process student grades and calculate statistics
    
    Args:
        student_records (list): List of dicts with 'name' and 'grades' (list)
    
    Returns:
        dict: Statistics including best_student, worst_student, class_average
        
    Example:
        >>> records = [
        ...     {'name': 'Alice', 'grades': [85, 90, 92]},
        ...     {'name': 'Bob', 'grades': [78, 85, 80]}
        ... ]
        >>> student_grades_accumulator(records)
        {'best_student': 'Alice', 'worst_student': 'Bob', 'class_average': 85.0}
    """
    if not student_records:
        return {'best_student': None, 'worst_student': None, 'class_average': 0}
    
    best_student = None
    worst_student = None
    best_avg = -1
    worst_avg = 101
    total_class_points = 0
    total_class_grades = 0
    
    for student in student_records:
        # Calculate student's average
        student_total = 0
        for grade in student['grades']:
            student_total += grade
            total_class_points += grade
            total_class_grades += 1
        
        student_avg = student_total / len(student['grades']) if student['grades'] else 0
        
        # Track best and worst students
        if student_avg > best_avg:
            best_avg = student_avg
            best_student = student['name']
        
        if student_avg < worst_avg:
            worst_avg = student_avg
            worst_student = student['name']
    
    class_average = total_class_points / total_class_grades if total_class_grades else 0
    
    return {
        'best_student': best_student,
        'worst_student': worst_student,
        'class_average': round(class_average, 1)
    }


def text_analysis_accumulator(text):
    """
    Text processing example: Analyze text using multiple accumulators
    
    Args:
        text (str): Input text to analyze
    
    Returns:
        dict: Analysis with word_count, char_count, sentence_count, avg_word_length
        
    Example:
        >>> text_analysis_accumulator("Hello world. How are you?")
        {'word_count': 5, 'char_count': 26, 'sentence_count': 2, 'avg_word_length': 3.4}
    """
    word_count = 0
    char_count = 0
    sentence_count = 0
    total_word_length = 0
    
    # Process each character
    current_word = ""
    
    for char in text:
        char_count += 1
        
        if char.isalpha():
            current_word += char
        else:
            if current_word:  # End of word
                word_count += 1
                total_word_length += len(current_word)
                current_word = ""
            
            if char in '.!?':
                sentence_count += 1
    
    # Handle last word if text doesn't end with punctuation
    if current_word:
        word_count += 1
        total_word_length += len(current_word)
    
    avg_word_length = total_word_length / word_count if word_count > 0 else 0
    
    return {
        'word_count': word_count,
        'char_count': char_count,
        'sentence_count': sentence_count,
        'avg_word_length': round(avg_word_length, 1)
    }


def inventory_management_accumulator(transactions):
    """
    Business example: Track inventory using accumulator pattern
    
    Args:
        transactions (list): List of dicts with 'item', 'type' ('in'/'out'), 'quantity'
    
    Returns:
        dict: Current inventory levels for each item
        
    Example:
        >>> transactions = [
        ...     {'item': 'Apple', 'type': 'in', 'quantity': 100},
        ...     {'item': 'Apple', 'type': 'out', 'quantity': 30},
        ...     {'item': 'Banana', 'type': 'in', 'quantity': 50}
        ... ]
        >>> inventory_management_accumulator(transactions)
        {'Apple': 70, 'Banana': 50}
    """
    inventory = {}
    
    for transaction in transactions:
        item = transaction['item']
        quantity = transaction['quantity']
        
        # Initialize item if not exists
        if item not in inventory:
            inventory[item] = 0
        
        # Update inventory based on transaction type
        if transaction['type'] == 'in':
            inventory[item] += quantity
        elif transaction['type'] == 'out':
            inventory[item] -= quantity
            # Prevent negative inventory
            if inventory[item] < 0:
                inventory[item] = 0
    
    return inventory


def weather_data_accumulator(weather_records):
    """
    Data science example: Analyze weather data
    
    Args:
        weather_records (list): List of dicts with 'date', 'temperature', 'humidity'
    
    Returns:
        dict: Weather statistics
        
    Example:
        >>> records = [
        ...     {'date': '2023-01-01', 'temperature': 20, 'humidity': 60},
        ...     {'date': '2023-01-02', 'temperature': 25, 'humidity': 55}
        ... ]
        >>> weather_data_accumulator(records)
        {'avg_temp': 22.5, 'max_temp': 25, 'min_temp': 20, 'avg_humidity': 57.5}
    """
    if not weather_records:
        return {'avg_temp': 0, 'max_temp': 0, 'min_temp': 0, 'avg_humidity': 0}
    
    temp_sum = 0
    humidity_sum = 0
    max_temp = weather_records[0]['temperature']
    min_temp = weather_records[0]['temperature']
    
    for record in weather_records:
        temp = record['temperature']
        humidity = record['humidity']
        
        temp_sum += temp
        humidity_sum += humidity
        
        if temp > max_temp:
            max_temp = temp
        if temp < min_temp:
            min_temp = temp
    
    count = len(weather_records)
    
    return {
        'avg_temp': round(temp_sum / count, 1),
        'max_temp': max_temp,
        'min_temp': min_temp,
        'avg_humidity': round(humidity_sum / count, 1)
    }


def matrix_sum_accumulator(matrix):
    """
    2D data structure example: Sum all elements in a 2D matrix
    
    Args:
        matrix (list): 2D list (list of lists) containing numbers
    
    Returns:
        int/float: Sum of all elements in the matrix
        
    Example:
        >>> matrix_sum_accumulator([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        45
    """
    total = 0
    
    for row in matrix:
        for element in row:
            total += element
    
    return total


def fibonacci_accumulator(n):
    """
    Sequence generation example: Generate first n Fibonacci numbers
    
    Args:
        n (int): Number of Fibonacci numbers to generate
    
    Returns:
        list: First n Fibonacci numbers
        
    Example:
        >>> fibonacci_accumulator(8)
        [0, 1, 1, 2, 3, 5, 8, 13]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence


def challenge_exercises():
    """
    Challenge exercises for advanced accumulator practice
    These are left as TODOs for students to implement
    """
    
    def challenge_1_prime_accumulator(numbers):
        """
        Challenge 1: Count prime numbers in a list
        
        Args:
            numbers (list): List of integers
        
        Returns:
            int: Count of prime numbers
        """
        # TODO: Implement this using accumulator pattern
        # Hint: You'll need a helper function to check if a number is prime
        pass
    
    def challenge_2_nested_dict_sum(data, key):
        """
        Challenge 2: Sum values from nested dictionaries
        
        Args:
            data (list): List of dictionaries
            key (str): Key to sum values for
        
        Returns:
            int/float: Sum of all values for the given key
        
        Example:
            >>> data = [{'sales': 100, 'costs': 50}, {'sales': 200, 'costs': 75}]
            >>> challenge_2_nested_dict_sum(data, 'sales')
            300
        """
        # TODO: Implement this using accumulator pattern
        pass
    
    def challenge_3_moving_average(numbers, window_size):
        """
        Challenge 3: Calculate moving average with given window size
        
        Args:
            numbers (list): List of numbers
            window_size (int): Size of moving window
        
        Returns:
            list: List of moving averages
        
        Example:
            >>> challenge_3_moving_average([1, 2, 3, 4, 5], 3)
            [2.0, 3.0, 4.0]
        """
        # TODO: Implement this using accumulator pattern
        pass


def demonstrate_advanced_exercises():
    """
    Demonstrate all advanced accumulator examples
    """
    print("=== ADVANCED ACCUMULATOR DEMONSTRATIONS ===\n")
    
    # Sales analysis
    print("1. Sales Analysis:")
    sales_data = [
        {'product': 'Apple', 'price': 1.0, 'quantity': 10},
        {'product': 'Banana', 'price': 0.5, 'quantity': 20},
        {'product': 'Orange', 'price': 0.8, 'quantity': 15}
    ]
    result = sales_analysis_accumulator(sales_data)
    print(f"   Sales data: {len(sales_data)} products")
    print(f"   Results: {result}\n")
    
    # Student grades
    print("2. Student Grades Analysis:")
    students = [
        {'name': 'Alice', 'grades': [85, 90, 92, 88]},
        {'name': 'Bob', 'grades': [78, 85, 80, 82]},
        {'name': 'Charlie', 'grades': [95, 92, 98, 94]}
    ]
    grades_result = student_grades_accumulator(students)
    print(f"   Students: {len(students)}")
    print(f"   Results: {grades_result}\n")
    
    # Text analysis
    print("3. Text Analysis:")
    sample_text = "Hello world! How are you today? Python is awesome."
    text_result = text_analysis_accumulator(sample_text)
    print(f"   Text: '{sample_text}'")
    print(f"   Results: {text_result}\n")
    
    # Inventory management
    print("4. Inventory Management:")
    transactions = [
        {'item': 'Apple', 'type': 'in', 'quantity': 100},
        {'item': 'Apple', 'type': 'out', 'quantity': 30},
        {'item': 'Banana', 'type': 'in', 'quantity': 50},
        {'item': 'Banana', 'type': 'out', 'quantity': 10}
    ]
    inventory_result = inventory_management_accumulator(transactions)
    print(f"   Transactions: {len(transactions)}")
    print(f"   Final inventory: {inventory_result}\n")
    
    # Weather data
    print("5. Weather Data Analysis:")
    weather_data = [
        {'date': '2023-01-01', 'temperature': 20, 'humidity': 60},
        {'date': '2023-01-02', 'temperature': 25, 'humidity': 55},
        {'date': '2023-01-03', 'temperature': 18, 'humidity': 70}
    ]
    weather_result = weather_data_accumulator(weather_data)
    print(f"   Weather records: {len(weather_data)} days")
    print(f"   Results: {weather_result}\n")
    
    # Matrix sum
    print("6. Matrix Sum:")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_result = matrix_sum_accumulator(matrix)
    print(f"   Matrix: {matrix}")
    print(f"   Sum: {matrix_result}\n")
    
    # Fibonacci sequence
    print("7. Fibonacci Sequence:")
    fib_result = fibonacci_accumulator(10)
    print(f"   First 10 Fibonacci numbers: {fib_result}\n")


if __name__ == "__main__":
    demonstrate_advanced_exercises()