"""
Unit tests for the accumulators module.

This module contains comprehensive tests for all accumulator classes and utility functions.
"""

import unittest
from accumulators import (
    SumAccumulator, ProductAccumulator, ListAccumulator, CounterAccumulator,
    MinMaxAccumulator, CustomAccumulator, accumulate_sum, accumulate_product,
    accumulate_counts, accumulate_min_max
)


class TestSumAccumulator(unittest.TestCase):
    """Test cases for SumAccumulator."""
    
    def setUp(self):
        self.acc = SumAccumulator()
    
    def test_initial_value_default(self):
        """Test default initial value."""
        self.assertEqual(self.acc.get_result(), 0)
    
    def test_initial_value_custom(self):
        """Test custom initial value."""
        acc = SumAccumulator(10)
        self.assertEqual(acc.get_result(), 10)
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        self.acc.add(5)
        self.acc.add(3)
        self.assertEqual(self.acc.get_result(), 8)
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        self.acc.add(-5)
        self.acc.add(-3)
        self.assertEqual(self.acc.get_result(), -8)
    
    def test_add_mixed_numbers(self):
        """Test adding mixed positive and negative numbers."""
        self.acc.add(10)
        self.acc.add(-3)
        self.acc.add(5)
        self.assertEqual(self.acc.get_result(), 12)
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        self.acc.add(2.5)
        self.acc.add(3.7)
        self.assertAlmostEqual(self.acc.get_result(), 6.2)
    
    def test_reset(self):
        """Test resetting the accumulator."""
        self.acc.add(10)
        self.acc.reset()
        self.assertEqual(self.acc.get_result(), 0)


class TestProductAccumulator(unittest.TestCase):
    """Test cases for ProductAccumulator."""
    
    def setUp(self):
        self.acc = ProductAccumulator()
    
    def test_initial_value_default(self):
        """Test default initial value."""
        self.assertEqual(self.acc.get_result(), 1)
    
    def test_initial_value_custom(self):
        """Test custom initial value."""
        acc = ProductAccumulator(5)
        self.assertEqual(acc.get_result(), 5)
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        self.acc.multiply(3)
        self.acc.multiply(4)
        self.assertEqual(self.acc.get_result(), 12)
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        self.acc.multiply(5)
        self.acc.multiply(0)
        self.assertEqual(self.acc.get_result(), 0)
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        self.acc.multiply(-2)
        self.acc.multiply(3)
        self.assertEqual(self.acc.get_result(), -6)
    
    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        self.acc.multiply(2.5)
        self.acc.multiply(4.0)
        self.assertAlmostEqual(self.acc.get_result(), 10.0)
    
    def test_reset(self):
        """Test resetting the accumulator."""
        self.acc.multiply(10)
        self.acc.reset()
        self.assertEqual(self.acc.get_result(), 1)


class TestListAccumulator(unittest.TestCase):
    """Test cases for ListAccumulator."""
    
    def setUp(self):
        self.acc = ListAccumulator()
    
    def test_initial_state(self):
        """Test initial empty state."""
        self.assertEqual(self.acc.get_result(), [])
    
    def test_append_single_item(self):
        """Test appending a single item."""
        self.acc.append("hello")
        self.assertEqual(self.acc.get_result(), ["hello"])
    
    def test_append_multiple_items(self):
        """Test appending multiple items."""
        self.acc.append(1)
        self.acc.append("hello")
        self.acc.append([1, 2, 3])
        self.assertEqual(self.acc.get_result(), [1, "hello", [1, 2, 3]])
    
    def test_extend_with_list(self):
        """Test extending with a list."""
        self.acc.extend([1, 2, 3])
        self.assertEqual(self.acc.get_result(), [1, 2, 3])
    
    def test_append_and_extend(self):
        """Test combination of append and extend."""
        self.acc.append("start")
        self.acc.extend([1, 2, 3])
        self.acc.append("end")
        self.assertEqual(self.acc.get_result(), ["start", 1, 2, 3, "end"])
    
    def test_get_result_returns_copy(self):
        """Test that get_result returns a copy, not reference."""
        self.acc.append(1)
        result1 = self.acc.get_result()
        result1.append(2)
        result2 = self.acc.get_result()
        self.assertEqual(result2, [1])  # Original unchanged
    
    def test_reset(self):
        """Test resetting the accumulator."""
        self.acc.append(1)
        self.acc.append(2)
        self.acc.reset()
        self.assertEqual(self.acc.get_result(), [])


class TestCounterAccumulator(unittest.TestCase):
    """Test cases for CounterAccumulator."""
    
    def setUp(self):
        self.acc = CounterAccumulator()
    
    def test_initial_state(self):
        """Test initial empty state."""
        self.assertEqual(self.acc.get_result(), {})
    
    def test_count_single_item(self):
        """Test counting a single item."""
        self.acc.count("apple")
        self.assertEqual(self.acc.get_result(), {"apple": 1})
    
    def test_count_multiple_same_items(self):
        """Test counting the same item multiple times."""
        self.acc.count("apple")
        self.acc.count("apple")
        self.acc.count("apple")
        self.assertEqual(self.acc.get_result(), {"apple": 3})
    
    def test_count_different_items(self):
        """Test counting different items."""
        self.acc.count("apple")
        self.acc.count("banana")
        self.acc.count("apple")
        expected = {"apple": 2, "banana": 1}
        self.assertEqual(self.acc.get_result(), expected)
    
    def test_count_many(self):
        """Test counting many items at once."""
        items = ["a", "b", "a", "c", "b", "a"]
        self.acc.count_many(items)
        expected = {"a": 3, "b": 2, "c": 1}
        self.assertEqual(self.acc.get_result(), expected)
    
    def test_get_count(self):
        """Test getting count for specific item."""
        self.acc.count("apple")
        self.acc.count("apple")
        self.assertEqual(self.acc.get_count("apple"), 2)
        self.assertEqual(self.acc.get_count("banana"), 0)  # Default for missing
    
    def test_reset(self):
        """Test resetting the accumulator."""
        self.acc.count("apple")
        self.acc.reset()
        self.assertEqual(self.acc.get_result(), {})


class TestMinMaxAccumulator(unittest.TestCase):
    """Test cases for MinMaxAccumulator."""
    
    def setUp(self):
        self.acc = MinMaxAccumulator()
    
    def test_initial_state(self):
        """Test initial state."""
        self.assertIsNone(self.acc.get_min())
        self.assertIsNone(self.acc.get_max())
        self.assertEqual(self.acc.get_result(), (None, None))
    
    def test_single_value(self):
        """Test with single value."""
        self.acc.add(5)
        self.assertEqual(self.acc.get_min(), 5)
        self.assertEqual(self.acc.get_max(), 5)
        self.assertEqual(self.acc.get_result(), (5, 5))
    
    def test_multiple_values_ascending(self):
        """Test with multiple values in ascending order."""
        values = [1, 3, 5, 7, 9]
        for value in values:
            self.acc.add(value)
        self.assertEqual(self.acc.get_min(), 1)
        self.assertEqual(self.acc.get_max(), 9)
        self.assertEqual(self.acc.get_result(), (1, 9))
    
    def test_multiple_values_descending(self):
        """Test with multiple values in descending order."""
        values = [9, 7, 5, 3, 1]
        for value in values:
            self.acc.add(value)
        self.assertEqual(self.acc.get_min(), 1)
        self.assertEqual(self.acc.get_max(), 9)
    
    def test_duplicate_values(self):
        """Test with duplicate values."""
        values = [5, 2, 8, 2, 8, 1, 8]
        for value in values:
            self.acc.add(value)
        self.assertEqual(self.acc.get_min(), 1)
        self.assertEqual(self.acc.get_max(), 8)
    
    def test_negative_values(self):
        """Test with negative values."""
        values = [-5, -2, -8, -1]
        for value in values:
            self.acc.add(value)
        self.assertEqual(self.acc.get_min(), -8)
        self.assertEqual(self.acc.get_max(), -1)
    
    def test_reset(self):
        """Test resetting the accumulator."""
        self.acc.add(10)
        self.acc.reset()
        self.assertIsNone(self.acc.get_min())
        self.assertIsNone(self.acc.get_max())


class TestCustomAccumulator(unittest.TestCase):
    """Test cases for CustomAccumulator."""
    
    def test_string_concatenation(self):
        """Test custom accumulator for string concatenation."""
        acc = CustomAccumulator("", lambda a, b: a + b)
        acc.add("Hello")
        acc.add(" ")
        acc.add("World")
        self.assertEqual(acc.get_result(), "Hello World")
    
    def test_list_accumulation(self):
        """Test custom accumulator for list building."""
        acc = CustomAccumulator([], lambda a, b: a + [b])
        acc.add(1)
        acc.add(2)
        acc.add(3)
        self.assertEqual(acc.get_result(), [1, 2, 3])
    
    def test_max_accumulation(self):
        """Test custom accumulator for finding maximum."""
        acc = CustomAccumulator(float('-inf'), max)
        acc.add(3)
        acc.add(7)
        acc.add(2)
        self.assertEqual(acc.get_result(), 7)
    
    def test_reset(self):
        """Test resetting custom accumulator."""
        acc = CustomAccumulator(0, lambda a, b: a + b)
        acc.add(5)
        acc.reset()
        self.assertEqual(acc.get_result(), 0)


class TestUtilityFunctions(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_accumulate_sum(self):
        """Test sum utility function."""
        values = [1, 2, 3, 4, 5]
        result = accumulate_sum(values)
        self.assertEqual(result, 15)
    
    def test_accumulate_product(self):
        """Test product utility function."""
        values = [2, 3, 4]
        result = accumulate_product(values)
        self.assertEqual(result, 24)
    
    def test_accumulate_counts(self):
        """Test counts utility function."""
        items = ['a', 'b', 'a', 'c', 'b', 'a']
        result = accumulate_counts(items)
        expected = {'a': 3, 'b': 2, 'c': 1}
        self.assertEqual(result, expected)
    
    def test_accumulate_min_max(self):
        """Test min/max utility function."""
        values = [3, 7, 2, 9, 1, 8, 4]
        result = accumulate_min_max(values)
        self.assertEqual(result, (1, 9))
    
    def test_empty_lists(self):
        """Test utility functions with empty lists."""
        self.assertEqual(accumulate_sum([]), 0)
        self.assertEqual(accumulate_product([]), 1)
        self.assertEqual(accumulate_counts([]), {})
        self.assertEqual(accumulate_min_max([]), (None, None))


if __name__ == "__main__":
    unittest.main()