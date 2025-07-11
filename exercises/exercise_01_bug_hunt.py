"""
Exercise 1: Bug Hunt with Print Debugging

This file contains several bugs that you need to find and fix using
print debugging techniques. Practice strategic print statement placement
to identify and resolve the issues.

Instructions:
1. Run this file and observe the unexpected behavior
2. Add print statements to track down the bugs
3. Fix the bugs once you've identified them
4. Clean up your debug prints when done

Expected behavior:
- calculate_grade should return correct letter grades
- process_orders should handle all orders correctly
- find_common_elements should return intersection of lists
- bank_transfer should handle transfers properly
"""


def calculate_grade(score):
    """
    Calculate letter grade from numeric score.
    BUG: This function has logic errors in grade boundaries.
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B' 
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def process_orders(orders):
    """
    Process a list of orders and calculate total revenue.
    BUG: This function has issues with data handling.
    """
    total_revenue = 0
    processed_count = 0
    
    for order in orders:
        # Calculate order total
        order_total = order['quantity'] * order['price']
        total_revenue += order_total
        processed_count += 1
    
    return {
        'total_revenue': total_revenue,
        'processed_count': processed_count,
        'average_order': total_revenue / processed_count
    }


def find_common_elements(list1, list2):
    """
    Find common elements between two lists.
    BUG: This function doesn't work correctly for all cases.
    """
    common = []
    
    for item in list1:
        if item in list2:
            common.append(item)
    
    return common


def bank_transfer(from_account, to_account, amount):
    """
    Transfer money between bank accounts.
    BUG: This function has a critical logic error.
    """
    if from_account['balance'] >= amount:
        from_account['balance'] -= amount
        to_account['balance'] -= amount  # BUG: Should be += amount
        return True
    return False


def run_tests():
    """Run test cases to demonstrate the bugs."""
    print("🐛 Bug Hunt Exercise - Find and Fix the Bugs!")
    print("="*50)
    
    # Test 1: Grade calculation
    print("\n--- Test 1: Grade Calculation ---")
    test_scores = [95, 85, 75, 65, 55]
    expected_grades = ['A', 'B', 'C', 'D', 'F']
    
    for score, expected in zip(test_scores, expected_grades):
        result = calculate_grade(score)
        status = "✅" if result == expected else "❌"
        print(f"{status} Score {score}: got '{result}', expected '{expected}'")
    
    # Test 2: Order processing
    print("\n--- Test 2: Order Processing ---")
    orders = [
        {'id': 1, 'quantity': 2, 'price': 10.99},
        {'id': 2, 'quantity': 1, 'price': 25.50},
        {'id': 3, 'quantity': 3, 'price': 8.75},
    ]
    
    try:
        result = process_orders(orders)
        expected_revenue = (2 * 10.99) + (1 * 25.50) + (3 * 8.75)
        print(f"Expected revenue: ${expected_revenue:.2f}")
        print(f"Calculated revenue: ${result['total_revenue']:.2f}")
        print(f"Processed count: {result['processed_count']}")
        print(f"Average order: ${result['average_order']:.2f}")
    except Exception as e:
        print(f"❌ Error processing orders: {e}")
    
    # Test 3: Common elements
    print("\n--- Test 3: Common Elements ---")
    list_a = [1, 2, 3, 4, 5]
    list_b = [3, 4, 5, 6, 7]
    
    result = find_common_elements(list_a, list_b)
    expected = [3, 4, 5]
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Common elements: {result}")
    print(f"Expected: {expected}")
    print(f"Correct: {'✅' if result == expected else '❌'}")
    
    # Test 4: Bank transfer
    print("\n--- Test 4: Bank Transfer ---")
    account_a = {'name': 'Alice', 'balance': 1000.00}
    account_b = {'name': 'Bob', 'balance': 500.00}
    
    print(f"Before transfer:")
    print(f"  Alice: ${account_a['balance']:.2f}")
    print(f"  Bob: ${account_b['balance']:.2f}")
    
    transfer_success = bank_transfer(account_a, account_b, 200.00)
    
    print(f"After transferring $200 from Alice to Bob:")
    print(f"  Alice: ${account_a['balance']:.2f}")
    print(f"  Bob: ${account_b['balance']:.2f}")
    print(f"Transfer successful: {transfer_success}")
    
    # Expected: Alice should have $800, Bob should have $700


# TODO: Add your debug print statements to the functions above
# TODO: Identify and fix the bugs
# TODO: Clean up debug prints when done

if __name__ == "__main__":
    run_tests()
    
    print("\n" + "="*50)
    print("🎯 YOUR MISSION:")
    print("1. Add print statements to debug the failing functions")
    print("2. Identify the root cause of each bug")
    print("3. Fix the bugs")
    print("4. Verify all tests pass")
    print("5. Clean up debug prints")
    print("="*50)
