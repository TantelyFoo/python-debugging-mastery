"""
Print Debugging Strategies and Best Practices

This module demonstrates effective print statement debugging techniques.
Print debugging is often the first debugging tool developers reach for,
and when used strategically, it can be incredibly effective.
"""

import sys
import time
from datetime import datetime


def debug_print(message, var_name=None, var_value=None, func_name=None):
    """
    Enhanced print function for debugging with context information.
    
    Args:
        message: Description of what's being debugged
        var_name: Name of variable being inspected
        var_value: Value of variable being inspected
        func_name: Name of function where debug occurs
    """
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    func_info = f"[{func_name}]" if func_name else ""
    
    if var_name and var_value is not None:
        print(f"🐛 {timestamp} {func_info} {message} - {var_name} = {var_value}")
    else:
        print(f"🐛 {timestamp} {func_info} {message}")


def basic_print_example():
    """Basic print debugging example."""
    print("=== Basic Print Debugging ===")
    
    numbers = [1, 2, 3, 4, 5]
    total = 0
    
    print(f"Starting calculation with numbers: {numbers}")
    
    for i, num in enumerate(numbers):
        print(f"Step {i+1}: Adding {num} to total {total}")
        total += num
        print(f"New total: {total}")
    
    print(f"Final result: {total}")


def strategic_print_example():
    """Strategic print debugging with context."""
    print("\n=== Strategic Print Debugging ===")
    
    def calculate_average(data):
        debug_print("Function started", func_name="calculate_average")
        debug_print("Input validation", "data", data, "calculate_average")
        
        if not data:
            debug_print("Empty data detected", func_name="calculate_average")
            return 0
        
        total = sum(data)
        debug_print("Sum calculated", "total", total, "calculate_average")
        
        count = len(data)
        debug_print("Count calculated", "count", count, "calculate_average")
        
        average = total / count
        debug_print("Average calculated", "average", average, "calculate_average")
        
        return average
    
    # Test with different inputs
    test_cases = [
        [1, 2, 3, 4, 5],
        [],
        [10],
        [1.5, 2.5, 3.5]
    ]
    
    for i, test_data in enumerate(test_cases):
        print(f"\n--- Test Case {i+1} ---")
        result = calculate_average(test_data)
        print(f"Result: {result}")


def conditional_debugging():
    """Example of conditional debugging output."""
    print("\n=== Conditional Debugging ===")
    
    DEBUG = True  # Toggle this to enable/disable debug output
    
    def debug_if_enabled(message, **kwargs):
        if DEBUG:
            debug_print(message, **kwargs)
    
    def process_orders(orders):
        debug_if_enabled("Processing orders started", func_name="process_orders")
        
        processed = []
        for i, order in enumerate(orders):
            debug_if_enabled(f"Processing order {i+1}", "order", order, "process_orders")
            
            # Simulate processing
            if order.get('amount', 0) > 0:
                processed_order = {
                    'id': order.get('id'),
                    'amount': order.get('amount'),
                    'status': 'processed'
                }
                processed.append(processed_order)
                debug_if_enabled("Order processed successfully", "processed_order", processed_order, "process_orders")
            else:
                debug_if_enabled("Order skipped - invalid amount", "order", order, "process_orders")
        
        debug_if_enabled("All orders processed", "total_processed", len(processed), "process_orders")
        return processed
    
    # Test data
    sample_orders = [
        {'id': 1, 'amount': 100},
        {'id': 2, 'amount': 0},
        {'id': 3, 'amount': 250},
        {'id': 4}  # Missing amount
    ]
    
    result = process_orders(sample_orders)
    print(f"Final processed orders: {len(result)}")


def performance_debugging():
    """Example of using print statements for performance debugging."""
    print("\n=== Performance Debugging ===")
    
    def timed_operation(operation_name):
        """Decorator to time operations."""
        def decorator(func):
            def wrapper(*args, **kwargs):
                start_time = time.time()
                print(f"⏱️  Starting {operation_name}...")
                
                result = func(*args, **kwargs)
                
                end_time = time.time()
                duration = end_time - start_time
                print(f"⏱️  {operation_name} completed in {duration:.4f} seconds")
                
                return result
            return wrapper
        return decorator
    
    @timed_operation("Data Processing")
    def process_large_dataset(size):
        print(f"📊 Processing dataset of size {size}")
        
        # Simulate data processing
        data = list(range(size))
        
        # Processing steps with timing
        step_start = time.time()
        filtered_data = [x for x in data if x % 2 == 0]
        step_time = time.time() - step_start
        print(f"  📈 Filtering completed in {step_time:.4f}s - {len(filtered_data)} items remain")
        
        step_start = time.time()
        squared_data = [x**2 for x in filtered_data]
        step_time = time.time() - step_start
        print(f"  📈 Squaring completed in {step_time:.4f}s")
        
        return sum(squared_data)
    
    # Test with different sizes
    for size in [1000, 10000, 100000]:
        result = process_large_dataset(size)
        print(f"Result for size {size}: {result}\n")


def error_debugging():
    """Example of using print statements to debug errors."""
    print("\n=== Error Debugging ===")
    
    def safe_divide(a, b):
        print(f"🔍 safe_divide called with a={a}, b={b}")
        
        try:
            print("🔍 Attempting division...")
            result = a / b
            print(f"🔍 Division successful: {result}")
            return result
        except ZeroDivisionError as e:
            print(f"❌ ZeroDivisionError caught: {e}")
            print(f"🔍 Returning None for a={a}, b={b}")
            return None
        except TypeError as e:
            print(f"❌ TypeError caught: {e}")
            print(f"🔍 Invalid types: a={type(a).__name__}, b={type(b).__name__}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {type(e).__name__}: {e}")
            return None
    
    # Test cases with different error scenarios
    test_cases = [
        (10, 2),      # Normal case
        (10, 0),      # Division by zero
        ("10", 2),    # Type error
        (10, "2"),    # Type error
        (None, 5),    # None value
    ]
    
    for a, b in test_cases:
        print(f"\n--- Testing: {a} / {b} ---")
        result = safe_divide(a, b)
        print(f"Result: {result}")


# Print debugging best practices summary
def print_debugging_tips():
    """Summary of print debugging best practices."""
    print("\n" + "="*50)
    print("🎯 PRINT DEBUGGING BEST PRACTICES")
    print("="*50)
    
    tips = [
        "1. Use descriptive labels with your print statements",
        "2. Include variable names and values for clarity",
        "3. Add timestamps for performance debugging",
        "4. Use function names to track execution flow",
        "5. Implement conditional debugging for production code",
        "6. Use consistent formatting for easy reading",
        "7. Clean up debug prints before committing code",
        "8. Consider using a debug flag to toggle output",
        "9. Print both input and output of functions",
        "10. Use different prefixes (🐛, ⏱️, ❌) for different types of debug info"
    ]
    
    for tip in tips:
        print(f"  {tip}")


if __name__ == "__main__":
    print("🐛 Python Print Debugging Tutorial")
    print("="*40)
    
    # Run all examples
    basic_print_example()
    strategic_print_example()
    conditional_debugging()
    performance_debugging()
    error_debugging()
    print_debugging_tips()
    
    print("\n✅ Print debugging tutorial completed!")
    print("Next: Learn about assert statements in 02_assert_statements.py")
