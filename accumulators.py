"""
Accumulator patterns for Python practice.

This module demonstrates various accumulator patterns commonly used in Python
for collecting and processing data iteratively.
"""

from typing import Any, List, Union, Callable, Optional
from collections import defaultdict


class SumAccumulator:
    """Accumulates numeric values by summing them."""
    
    def __init__(self, initial_value: Union[int, float] = 0):
        self.total = initial_value
    
    def add(self, value: Union[int, float]) -> None:
        """Add a value to the sum."""
        self.total += value
    
    def get_result(self) -> Union[int, float]:
        """Get the current sum."""
        return self.total
    
    def reset(self) -> None:
        """Reset the accumulator to initial value."""
        self.total = 0


class ProductAccumulator:
    """Accumulates numeric values by multiplying them."""
    
    def __init__(self, initial_value: Union[int, float] = 1):
        self.product = initial_value
    
    def multiply(self, value: Union[int, float]) -> None:
        """Multiply the current product by a value."""
        self.product *= value
    
    def get_result(self) -> Union[int, float]:
        """Get the current product."""
        return self.product
    
    def reset(self) -> None:
        """Reset the accumulator to initial value."""
        self.product = 1


class ListAccumulator:
    """Accumulates values into a list."""
    
    def __init__(self):
        self.items = []
    
    def append(self, value: Any) -> None:
        """Append a value to the list."""
        self.items.append(value)
    
    def extend(self, values: List[Any]) -> None:
        """Extend the list with multiple values."""
        self.items.extend(values)
    
    def get_result(self) -> List[Any]:
        """Get the current list."""
        return self.items.copy()
    
    def reset(self) -> None:
        """Reset the accumulator to empty list."""
        self.items = []


class CounterAccumulator:
    """Accumulates counts of items."""
    
    def __init__(self):
        self.counts = defaultdict(int)
    
    def count(self, item: Any) -> None:
        """Increment the count for an item."""
        self.counts[item] += 1
    
    def count_many(self, items: List[Any]) -> None:
        """Count multiple items."""
        for item in items:
            self.count(item)
    
    def get_result(self) -> dict:
        """Get the current counts as a dictionary."""
        return dict(self.counts)
    
    def get_count(self, item: Any) -> int:
        """Get the count for a specific item."""
        return self.counts[item]
    
    def reset(self) -> None:
        """Reset all counts to zero."""
        self.counts = defaultdict(int)


class MinMaxAccumulator:
    """Accumulates minimum and maximum values."""
    
    def __init__(self):
        self.min_value = None
        self.max_value = None
    
    def add(self, value: Union[int, float]) -> None:
        """Add a value and update min/max."""
        if self.min_value is None or value < self.min_value:
            self.min_value = value
        if self.max_value is None or value > self.max_value:
            self.max_value = value
    
    def get_min(self) -> Optional[Union[int, float]]:
        """Get the minimum value."""
        return self.min_value
    
    def get_max(self) -> Optional[Union[int, float]]:
        """Get the maximum value."""
        return self.max_value
    
    def get_result(self) -> tuple:
        """Get both min and max as a tuple."""
        return (self.min_value, self.max_value)
    
    def reset(self) -> None:
        """Reset the accumulator."""
        self.min_value = None
        self.max_value = None


class CustomAccumulator:
    """Generic accumulator that applies a custom function."""
    
    def __init__(self, initial_value: Any, accumulate_func: Callable[[Any, Any], Any]):
        self.value = initial_value
        self.initial_value = initial_value
        self.accumulate_func = accumulate_func
    
    def add(self, new_value: Any) -> None:
        """Add a value using the custom accumulate function."""
        self.value = self.accumulate_func(self.value, new_value)
    
    def get_result(self) -> Any:
        """Get the current accumulated value."""
        return self.value
    
    def reset(self) -> None:
        """Reset the accumulator to initial value."""
        self.value = self.initial_value


# Utility functions for common accumulation patterns
def accumulate_sum(values: List[Union[int, float]]) -> Union[int, float]:
    """Utility function to sum values using accumulator pattern."""
    acc = SumAccumulator()
    for value in values:
        acc.add(value)
    return acc.get_result()


def accumulate_product(values: List[Union[int, float]]) -> Union[int, float]:
    """Utility function to calculate product using accumulator pattern."""
    acc = ProductAccumulator()
    for value in values:
        acc.multiply(value)
    return acc.get_result()


def accumulate_counts(items: List[Any]) -> dict:
    """Utility function to count items using accumulator pattern."""
    acc = CounterAccumulator()
    acc.count_many(items)
    return acc.get_result()


def accumulate_min_max(values: List[Union[int, float]]) -> tuple:
    """Utility function to find min and max using accumulator pattern."""
    acc = MinMaxAccumulator()
    for value in values:
        acc.add(value)
    return acc.get_result()


if __name__ == "__main__":
    # Example usage
    print("=== Accumulator Examples ===")
    
    # Sum accumulator example
    sum_acc = SumAccumulator()
    for i in range(1, 6):
        sum_acc.add(i)
    print(f"Sum of 1-5: {sum_acc.get_result()}")
    
    # Product accumulator example
    product_acc = ProductAccumulator()
    for i in range(1, 6):
        product_acc.multiply(i)
    print(f"Product of 1-5: {product_acc.get_result()}")
    
    # List accumulator example
    list_acc = ListAccumulator()
    for i in range(5):
        list_acc.append(i ** 2)
    print(f"Squares: {list_acc.get_result()}")
    
    # Counter accumulator example
    counter_acc = CounterAccumulator()
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    counter_acc.count_many(words)
    print(f"Word counts: {counter_acc.get_result()}")
    
    # Min/Max accumulator example
    minmax_acc = MinMaxAccumulator()
    values = [3, 7, 2, 9, 1, 8, 4]
    for value in values:
        minmax_acc.add(value)
    print(f"Min/Max of {values}: {minmax_acc.get_result()}")
    
    # Custom accumulator example (concatenate strings)
    concat_acc = CustomAccumulator("", lambda acc, val: acc + str(val) + " ")
    for word in ["Hello", "world", "from", "Python"]:
        concat_acc.add(word)
    print(f"Concatenated: '{concat_acc.get_result().strip()}'")