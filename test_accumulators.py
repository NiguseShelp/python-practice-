#!/usr/bin/env python3
"""
Test Runner for Accumulator Practice

This script runs basic tests on the accumulator functions to ensure they work correctly.
It's designed to be simple and educational rather than comprehensive.
"""

import sys
from accumulator_practice import *
from advanced_accumulator_exercises import *


def test_basic_functions():
    """Test basic accumulator functions"""
    print("Testing basic accumulator functions...")
    
    # Test basic sum
    assert basic_sum_accumulator([1, 2, 3, 4, 5]) == 15
    assert basic_sum_accumulator([]) == 0
    assert basic_sum_accumulator([-1, 1, -2, 2]) == 0
    print("✓ basic_sum_accumulator passed")
    
    # Test product
    assert product_accumulator([2, 3, 4]) == 24
    assert product_accumulator([1, 1, 1, 1]) == 1
    assert product_accumulator([5]) == 5
    print("✓ product_accumulator passed")
    
    # Test count
    assert count_accumulator([1, 2, 3, 2, 4, 2], 2) == 3
    assert count_accumulator(['a', 'b', 'c', 'a'], 'a') == 2
    assert count_accumulator([1, 2, 3], 5) == 0
    print("✓ count_accumulator passed")
    
    # Test max/min
    assert max_accumulator([3, 7, 2, 9, 1]) == 9
    assert min_accumulator([3, 7, 2, 9, 1]) == 1
    assert max_accumulator([5]) == 5
    assert min_accumulator([5]) == 5
    print("✓ max_accumulator and min_accumulator passed")
    
    # Test string concatenation
    assert string_concatenation_accumulator(["Hello", "world"]) == "Hello world"
    assert string_concatenation_accumulator(["A"], "_") == "A"
    assert string_concatenation_accumulator([], "_") == ""
    print("✓ string_concatenation_accumulator passed")
    
    # Test list building
    evens = list_building_accumulator([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
    assert evens == [2, 4, 6]
    print("✓ list_building_accumulator passed")
    
    # Test average
    assert average_accumulator([1, 2, 3, 4, 5]) == 3.0
    assert average_accumulator([10]) == 10.0
    assert average_accumulator([]) == 0.0
    print("✓ average_accumulator passed")
    
    # Test nested sum
    assert nested_sum_accumulator([[1, 2], [3, 4, 5], [6]]) == 21
    assert nested_sum_accumulator([[], [1], []]) == 1
    print("✓ nested_sum_accumulator passed")
    
    # Test frequency counter
    freq = frequency_counter_accumulator(['a', 'b', 'a', 'c', 'b', 'a'])
    assert freq == {'a': 3, 'b': 2, 'c': 1}
    print("✓ frequency_counter_accumulator passed")
    
    # Test running sum
    assert running_sum_accumulator([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum_accumulator([5]) == [5]
    assert running_sum_accumulator([]) == []
    print("✓ running_sum_accumulator passed")


def test_exercise_functions():
    """Test exercise functions"""
    print("\nTesting exercise functions...")
    
    # Test sum of squares
    assert exercise_1_sum_of_squares([1, 2, 3]) == 14  # 1 + 4 + 9
    assert exercise_1_sum_of_squares([2, 2]) == 8  # 4 + 4
    print("✓ exercise_1_sum_of_squares passed")
    
    # Test longest word
    assert exercise_2_longest_word(["cat", "elephant", "dog"]) == "elephant"
    assert exercise_2_longest_word(["hello", "world"]) == "hello"  # Same length, first wins
    assert exercise_2_longest_word([]) == ""
    print("✓ exercise_2_longest_word passed")
    
    # Test alternating sum
    assert exercise_3_alternating_sum([1, 2, 3, 4]) == -2  # 1 - 2 + 3 - 4
    assert exercise_3_alternating_sum([5]) == 5
    assert exercise_3_alternating_sum([1, 1]) == 0  # 1 - 1
    print("✓ exercise_3_alternating_sum passed")
    
    # Test group by condition
    evens, odds = exercise_4_group_by_condition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    assert evens == [2, 4]
    assert odds == [1, 3, 5]
    print("✓ exercise_4_group_by_condition passed")


def test_advanced_functions():
    """Test advanced accumulator functions"""
    print("\nTesting advanced functions...")
    
    # Test sales analysis
    sales_data = [
        {'product': 'Apple', 'price': 1.0, 'quantity': 10},
        {'product': 'Banana', 'price': 0.5, 'quantity': 20}
    ]
    result = sales_analysis_accumulator(sales_data)
    assert result['total_revenue'] == 20.0  # (1.0 * 10) + (0.5 * 20)
    assert result['total_items'] == 30  # 10 + 20
    assert result['avg_price'] == 0.75  # (1.0 + 0.5) / 2
    print("✓ sales_analysis_accumulator passed")
    
    # Test text analysis
    text_result = text_analysis_accumulator("Hello world.")
    assert text_result['word_count'] == 2
    assert text_result['sentence_count'] == 1
    print("✓ text_analysis_accumulator passed")
    
    # Test inventory management
    transactions = [
        {'item': 'Apple', 'type': 'in', 'quantity': 100},
        {'item': 'Apple', 'type': 'out', 'quantity': 30}
    ]
    inventory = inventory_management_accumulator(transactions)
    assert inventory['Apple'] == 70
    print("✓ inventory_management_accumulator passed")
    
    # Test matrix sum
    matrix = [[1, 2], [3, 4]]
    assert matrix_sum_accumulator(matrix) == 10  # 1 + 2 + 3 + 4
    print("✓ matrix_sum_accumulator passed")
    
    # Test fibonacci
    fib = fibonacci_accumulator(5)
    assert fib == [0, 1, 1, 2, 3]
    print("✓ fibonacci_accumulator passed")


def run_demonstrations():
    """Run the demonstration functions"""
    print("\n" + "="*50)
    print("RUNNING DEMONSTRATIONS")
    print("="*50)
    
    print("\n--- Basic Accumulator Demonstrations ---")
    demonstration()
    
    print("\n--- Advanced Accumulator Demonstrations ---")
    demonstrate_advanced_exercises()


def main():
    """Main test runner"""
    print("ACCUMULATOR PRACTICE TEST RUNNER")
    print("="*50)
    
    try:
        test_basic_functions()
        test_exercise_functions()
        test_advanced_functions()
        
        print("\n" + "="*50)
        print("ALL TESTS PASSED! ✓")
        print("="*50)
        
        # Ask user if they want to see demonstrations
        print("\nWould you like to see the demonstrations? (y/n): ", end="")
        if input().lower().startswith('y'):
            run_demonstrations()
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()