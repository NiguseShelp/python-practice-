# Python Practice - Accumulators

A comprehensive Python implementation demonstrating various accumulator patterns for data collection and processing.

## Overview

This repository contains a complete implementation of accumulator patterns in Python, which are fundamental programming techniques for iteratively collecting and processing data. Accumulators are commonly used for tasks like calculating sums, building lists, counting items, and maintaining running statistics.

## Files

- `accumulators.py` - Main module with accumulator classes and utility functions
- `test_accumulators.py` - Comprehensive unit tests for all accumulator functionality
- `examples.py` - Practical examples showing real-world applications

## Accumulator Classes

### 1. SumAccumulator
Accumulates numeric values by summing them.
```python
sum_acc = SumAccumulator()
sum_acc.add(10)
sum_acc.add(20)
print(sum_acc.get_result())  # 30
```

### 2. ProductAccumulator
Accumulates numeric values by multiplying them.
```python
product_acc = ProductAccumulator()
product_acc.multiply(3)
product_acc.multiply(4)
print(product_acc.get_result())  # 12
```

### 3. ListAccumulator
Accumulates values into a list.
```python
list_acc = ListAccumulator()
list_acc.append("hello")
list_acc.extend(["world", "!"])
print(list_acc.get_result())  # ['hello', 'world', '!']
```

### 4. CounterAccumulator
Counts occurrences of items.
```python
counter_acc = CounterAccumulator()
counter_acc.count_many(["apple", "banana", "apple"])
print(counter_acc.get_result())  # {'apple': 2, 'banana': 1}
```

### 5. MinMaxAccumulator
Tracks minimum and maximum values.
```python
minmax_acc = MinMaxAccumulator()
for value in [3, 7, 2, 9, 1]:
    minmax_acc.add(value)
print(minmax_acc.get_result())  # (1, 9)
```

### 6. CustomAccumulator
Generic accumulator with custom function.
```python
# String concatenation example
concat_acc = CustomAccumulator("", lambda acc, val: acc + str(val) + " ")
for word in ["Hello", "world"]:
    concat_acc.add(word)
print(concat_acc.get_result().strip())  # "Hello world"
```

## Utility Functions

The module also provides convenient utility functions for common accumulation patterns:

- `accumulate_sum(values)` - Sum a list of values
- `accumulate_product(values)` - Calculate product of values
- `accumulate_counts(items)` - Count item occurrences
- `accumulate_min_max(values)` - Find min and max

## Usage Examples

### Basic Usage
```python
from accumulators import SumAccumulator, CounterAccumulator

# Sum numbers
sum_acc = SumAccumulator()
for i in range(1, 6):
    sum_acc.add(i)
print(f"Sum: {sum_acc.get_result()}")  # Sum: 15

# Count items
counter = CounterAccumulator()
words = ["apple", "banana", "apple", "cherry"]
counter.count_many(words)
print(f"Counts: {counter.get_result()}")  # Counts: {'apple': 2, 'banana': 1, 'cherry': 1}
```

### Real-World Applications

The `examples.py` file demonstrates practical applications:

1. **Grade Analysis** - Analyze student grades with statistics and letter grade distribution
2. **Sales Data Processing** - Process sales records with regional and product analysis
3. **Text Analysis** - Analyze text for word frequencies, lengths, and character statistics
4. **Running Statistics** - Calculate running averages using custom accumulators

## Running the Code

### Run Basic Examples
```bash
python3 accumulators.py
```

### Run Practical Examples
```bash
python3 examples.py
```

### Run Tests
```bash
python3 -m unittest test_accumulators.py -v
```

## Key Features

- **Object-Oriented Design** - Clean, reusable accumulator classes
- **Type Hints** - Full type annotations for better code clarity
- **Comprehensive Testing** - 44+ unit tests covering all functionality
- **Reset Functionality** - All accumulators can be reset for reuse
- **Practical Examples** - Real-world applications demonstrating usage
- **Utility Functions** - Convenient functions for common patterns
- **Custom Accumulators** - Extensible pattern for custom accumulation logic

## Learning Objectives

This implementation teaches:
- Accumulator design patterns
- Object-oriented programming in Python
- Type hints and documentation
- Unit testing with unittest
- Data processing techniques
- Functional programming concepts

## Common Use Cases

Accumulators are useful for:
- Data aggregation and statistics
- Building collections iteratively
- Counting and frequency analysis
- Running calculations (averages, totals)
- State management in algorithms
- Functional programming patterns