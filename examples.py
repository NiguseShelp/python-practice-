"""
Practical examples demonstrating accumulator patterns.

This module shows real-world applications of accumulator patterns
for data processing and analysis.
"""

from accumulators import (
    SumAccumulator, ProductAccumulator, ListAccumulator, CounterAccumulator,
    MinMaxAccumulator, CustomAccumulator
)


def analyze_grades(grades):
    """
    Analyze student grades using multiple accumulator patterns.
    
    Args:
        grades: List of numeric grades
        
    Returns:
        dict: Analysis results including sum, average, min, max, letter grade counts
    """
    if not grades:
        return {"error": "No grades provided"}
    
    # Use sum accumulator for total
    sum_acc = SumAccumulator()
    
    # Use min/max accumulator for range
    minmax_acc = MinMaxAccumulator()
    
    # Use counter for letter grades
    letter_acc = CounterAccumulator()
    
    # Use list accumulator for passing grades
    passing_acc = ListAccumulator()
    
    for grade in grades:
        sum_acc.add(grade)
        minmax_acc.add(grade)
        
        # Convert to letter grade
        if grade >= 90:
            letter = 'A'
        elif grade >= 80:
            letter = 'B'
        elif grade >= 70:
            letter = 'C'
        elif grade >= 60:
            letter = 'D'
        else:
            letter = 'F'
        
        letter_acc.count(letter)
        
        # Track passing grades (>= 60)
        if grade >= 60:
            passing_acc.append(grade)
    
    total = sum_acc.get_result()
    min_grade, max_grade = minmax_acc.get_result()
    
    return {
        "total_students": len(grades),
        "total_points": total,
        "average": total / len(grades),
        "min_grade": min_grade,
        "max_grade": max_grade,
        "letter_grades": letter_acc.get_result(),
        "passing_grades": passing_acc.get_result(),
        "passing_rate": len(passing_acc.get_result()) / len(grades) * 100
    }


def process_sales_data(sales_records):
    """
    Process sales data using accumulator patterns.
    
    Args:
        sales_records: List of dicts with 'amount', 'product', 'region' keys
        
    Returns:
        dict: Sales analysis results
    """
    if not sales_records:
        return {"error": "No sales data provided"}
    
    # Total revenue
    revenue_acc = SumAccumulator()
    
    # Product sales count
    product_acc = CounterAccumulator()
    
    # Regional sales totals
    region_totals = {}
    
    # Top sales (amounts >= 1000)
    big_sales_acc = ListAccumulator()
    
    # Sales range
    amount_range_acc = MinMaxAccumulator()
    
    for record in sales_records:
        amount = record['amount']
        product = record['product']
        region = record['region']
        
        # Accumulate totals
        revenue_acc.add(amount)
        product_acc.count(product)
        amount_range_acc.add(amount)
        
        # Regional totals using individual accumulators
        if region not in region_totals:
            region_totals[region] = SumAccumulator()
        region_totals[region].add(amount)
        
        # Track big sales
        if amount >= 1000:
            big_sales_acc.append(record)
    
    # Get final regional totals
    regional_results = {}
    for region, acc in region_totals.items():
        regional_results[region] = acc.get_result()
    
    min_sale, max_sale = amount_range_acc.get_result()
    
    return {
        "total_revenue": revenue_acc.get_result(),
        "total_transactions": len(sales_records),
        "average_sale": revenue_acc.get_result() / len(sales_records),
        "product_counts": product_acc.get_result(),
        "regional_totals": regional_results,
        "big_sales_count": len(big_sales_acc.get_result()),
        "sale_range": (min_sale, max_sale)
    }


def text_analysis(text):
    """
    Analyze text using accumulator patterns.
    
    Args:
        text: String to analyze
        
    Returns:
        dict: Text analysis results
    """
    if not text:
        return {"error": "No text provided"}
    
    words = text.lower().split()
    
    # Word frequency
    word_freq = CounterAccumulator()
    
    # Word lengths
    length_acc = ListAccumulator()
    length_range = MinMaxAccumulator()
    
    # Character count
    char_count = SumAccumulator()
    
    # Vowel count
    vowel_count = CounterAccumulator()
    vowels = 'aeiou'
    
    for word in words:
        word_freq.count(word)
        word_len = len(word)
        length_acc.append(word_len)
        length_range.add(word_len)
        char_count.add(word_len)
        
        # Count vowels in word
        for char in word:
            if char in vowels:
                vowel_count.count(char)
    
    lengths = length_acc.get_result()
    min_len, max_len = length_range.get_result()
    
    return {
        "word_count": len(words),
        "character_count": char_count.get_result(),
        "unique_words": len(word_freq.get_result()),
        "word_frequencies": word_freq.get_result(),
        "average_word_length": sum(lengths) / len(lengths) if lengths else 0,
        "word_length_range": (min_len, max_len),
        "vowel_counts": vowel_count.get_result()
    }


def running_statistics():
    """
    Demonstrate running statistics using custom accumulator.
    """
    # Custom accumulator for running average
    def update_average(current_avg_count, new_value):
        avg, count = current_avg_count
        count += 1
        avg = ((count - 1) * avg + new_value) / count
        return (avg, count)
    
    running_avg = CustomAccumulator((0.0, 0), update_average)
    
    print("=== Running Statistics Demo ===")
    values = [10, 20, 30, 15, 25, 35]
    
    for i, value in enumerate(values, 1):
        running_avg.add(value)
        avg, count = running_avg.get_result()
        print(f"After adding {value}: Running average = {avg:.2f} (n={count})")


if __name__ == "__main__":
    print("=== Practical Accumulator Examples ===\n")
    
    # Grade analysis example
    print("1. Grade Analysis:")
    grades = [85, 92, 78, 96, 67, 88, 79, 93, 84, 91]
    analysis = analyze_grades(grades)
    print(f"   Grades: {grades}")
    print(f"   Average: {analysis['average']:.1f}")
    print(f"   Range: {analysis['min_grade']} - {analysis['max_grade']}")
    print(f"   Letter grades: {analysis['letter_grades']}")
    print(f"   Passing rate: {analysis['passing_rate']:.1f}%\n")
    
    # Sales analysis example
    print("2. Sales Analysis:")
    sales = [
        {"amount": 1200, "product": "Laptop", "region": "North"},
        {"amount": 800, "product": "Phone", "region": "South"},
        {"amount": 1500, "product": "Laptop", "region": "North"},
        {"amount": 600, "product": "Tablet", "region": "East"},
        {"amount": 900, "product": "Phone", "region": "West"},
        {"amount": 2000, "product": "Laptop", "region": "South"}
    ]
    sales_analysis = process_sales_data(sales)
    print(f"   Total revenue: ${sales_analysis['total_revenue']:,}")
    print(f"   Average sale: ${sales_analysis['average_sale']:.0f}")
    print(f"   Product counts: {sales_analysis['product_counts']}")
    print(f"   Regional totals: {sales_analysis['regional_totals']}")
    print(f"   Big sales (>=1000): {sales_analysis['big_sales_count']}\n")
    
    # Text analysis example
    print("3. Text Analysis:")
    sample_text = "The quick brown fox jumps over the lazy dog"
    text_stats = text_analysis(sample_text)
    print(f"   Text: '{sample_text}'")
    print(f"   Words: {text_stats['word_count']}")
    print(f"   Characters: {text_stats['character_count']}")
    print(f"   Unique words: {text_stats['unique_words']}")
    print(f"   Average word length: {text_stats['average_word_length']:.1f}")
    print(f"   Most common vowel: {max(text_stats['vowel_counts'].items(), key=lambda x: x[1])}\n")
    
    # Running statistics example
    running_statistics()