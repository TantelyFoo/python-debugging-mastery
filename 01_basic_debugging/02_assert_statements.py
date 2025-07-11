"""
Assert Statements for Debugging and Validation

Assert statements are a powerful debugging tool that help catch bugs early
by validating assumptions about your code. They're perfect for catching
logic errors and ensuring that your functions receive valid inputs.
"""

import math
from typing import List, Dict, Any


def basic_assertions():
    """Demonstrate basic assert statement usage."""
    print("=== Basic Assert Statements ===")
    
    # Basic assertion
    x = 10
    assert x > 0, f"Expected positive number, got {x}"
    print(f"✅ x = {x} is positive")
    
    # Assertion with multiple conditions
    age = 25
    assert 0 <= age <= 120, (
        f"Invalid age: {age}. Age must be between 0 and 120"
    )
    print(f"✅ Age {age} is valid")
    
    # Type assertions
    name = "Alice"
    assert isinstance(name, str), f"Name must be a string, got {type(name)}"
    print(f"✅ Name '{name}' is a string")
    
    # Container assertions
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) > 0, "Numbers list cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), (
        "All items must be numbers"
    )
    print(f"✅ Numbers list {numbers} is valid")


def function_preconditions():
    """Using assertions for function preconditions."""
    print("\n=== Function Preconditions ===")
    
    def calculate_sqrt(number):
        """Calculate square root with precondition validation."""
        # Precondition assertions
        assert isinstance(number, (int, float)), \
            f"Input must be a number, got {type(number).__name__}"
        assert number >= 0, \
            f"Cannot calculate square root of negative number: {number}"
        
        result = math.sqrt(number)
        
        # Postcondition assertion
        assert result >= 0, "Square root should always be non-negative"
        
        return result
    
    # Test valid inputs
    test_values = [0, 1, 4, 9, 16, 25.5]
    for value in test_values:
        try:
            result = calculate_sqrt(value)
            print(f"✅ sqrt({value}) = {result}")
        except AssertionError as e:
            print(f"❌ Assertion failed for {value}: {e}")
    
    # Test invalid inputs (these will trigger assertions)
    print("\n--- Testing invalid inputs ---")
    invalid_values = [-1, "hello", None]
    for value in invalid_values:
        try:
            result = calculate_sqrt(value)
            print(f"⚠️  Unexpected success for {value}: {result}")
        except AssertionError as e:
            print(f"✅ Correctly caught invalid input {value}: {e}")
        except Exception as e:
            print(f"❌ Unexpected error for {value}: {e}")


def data_structure_validation():
    """Using assertions to validate data structures."""
    print("\n=== Data Structure Validation ===")
    
    def process_user_data(user_data: Dict[str, Any]):
        """Process user data with comprehensive validation."""
        print(f"Processing user data: {user_data}")
        
        # Required fields
        required_fields = ['id', 'name', 'email']
        for field in required_fields:
            assert field in user_data, f"Missing required field: {field}"
            assert user_data[field] is not None, (
                f"Field {field} cannot be None"
            )
        
        # Type validations
        assert isinstance(user_data['id'], int), \
            f"User ID must be integer, got {type(user_data['id'])}"
        assert isinstance(user_data['name'], str), \
            f"Name must be string, got {type(user_data['name'])}"
        assert isinstance(user_data['email'], str), \
            f"Email must be string, got {type(user_data['email'])}"
        
        # Value validations
        assert user_data['id'] > 0, (
            f"User ID must be positive, got {user_data['id']}"
        )
        assert len(user_data['name'].strip()) > 0, "Name cannot be empty"
        assert '@' in user_data['email'], (
            f"Invalid email format: {user_data['email']}"
        )
        
        # Optional field validations
        if 'age' in user_data:
            assert isinstance(user_data['age'], int), \
                f"Age must be integer, got {type(user_data['age'])}"
            assert 0 <= user_data['age'] <= 120, \
                f"Invalid age: {user_data['age']}"
        
        print("✅ User data validation passed")
        return True
    
    # Test cases
    valid_users = [
        {'id': 1, 'name': 'Alice Johnson', 'email': 'alice@example.com'},
        {'id': 2, 'name': 'Bob Smith', 'email': 'bob@test.org', 'age': 30},
    ]
    
    invalid_users = [
        {'name': 'No ID', 'email': 'test@example.com'},  # Missing ID
        # Invalid ID
        {'id': -1, 'name': 'Negative ID', 'email': 'test@example.com'},
        {'id': 1, 'name': '', 'email': 'test@example.com'},  # Empty name
        # Invalid email
        {'id': 1, 'name': 'John', 'email': 'invalid-email'},
        # Invalid age
        {'id': 1, 'name': 'Jane', 'email': 'jane@example.com', 'age': -5},
    ]
    
    print("--- Testing valid users ---")
    for user in valid_users:
        try:
            process_user_data(user)
        except AssertionError as e:
            print(f"❌ Unexpected assertion error: {e}")
    
    print("\n--- Testing invalid users ---")
    for user in invalid_users:
        try:
            process_user_data(user)
            print(f"⚠️  Unexpected success for invalid user: {user}")
        except AssertionError as e:
            print(f"✅ Correctly caught invalid user: {e}")


def list_processing_assertions():
    """Assertions for list processing functions."""
    print("\n=== List Processing Assertions ===")
    
    def find_max_value(numbers: List[float]) -> float:
        """Find maximum value with assertions."""
        # Input validation
        assert isinstance(numbers, list), (
            f"Input must be a list, got {type(numbers)}"
        )
        assert len(numbers) > 0, "Cannot find max of empty list"
        assert all(isinstance(n, (int, float)) for n in numbers), \
            "All elements must be numbers"
        
        max_val = max(numbers)
        
        # Postcondition: result should be in the list
        assert max_val in numbers, "Max value should be in the original list"
        
        return max_val
    
    def calculate_average(numbers: List[float]) -> float:
        """Calculate average with comprehensive validation."""
        # Preconditions
        assert isinstance(numbers, list), "Input must be a list"
        assert len(numbers) > 0, "Cannot calculate average of empty list"
        assert all(isinstance(n, (int, float)) for n in numbers), \
            "All elements must be numbers"
        
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        
        # Postconditions
        min_val = min(numbers)
        max_val = max(numbers)
        assert min_val <= average <= max_val, (
            f"Average {average} should be between "
            f"min {min_val} and max {max_val}"
        )
        
        return average
    
    # Test data
    test_cases = [
        [1, 2, 3, 4, 5],
        [10.5, 20.3, 15.7],
        [100],
        [-5, -10, -1],
        [0, 0, 0],
    ]
    
    for numbers in test_cases:
        try:
            max_val = find_max_value(numbers)
            avg_val = calculate_average(numbers)
            print(f"✅ {numbers}: max={max_val}, avg={avg_val:.2f}")
        except AssertionError as e:
            print(f"❌ Assertion failed for {numbers}: {e}")


def class_invariant_assertions():
    """Using assertions to maintain class invariants."""
    print("\n=== Class Invariant Assertions ===")
    
    class BankAccount:
        """Bank account with invariant assertions."""
        
        def __init__(self, account_number: str, initial_balance: float = 0.0):
            assert isinstance(account_number, str), (
                "Account number must be string"
            )
            assert len(account_number.strip()) > 0, (
                "Account number cannot be empty"
            )
            assert isinstance(initial_balance, (int, float)), (
                "Balance must be a number"
            )
            assert initial_balance >= 0, (
                "Initial balance cannot be negative"
            )
            
            self._account_number = account_number.strip()
            self._balance = float(initial_balance)
            self._transaction_count = 0
            
            self._check_invariants()
        
        def _check_invariants(self):
            """Check class invariants."""
            assert isinstance(self._balance, (int, float)), (
                "Balance must be numeric"
            )
            assert self._balance >= 0, (
                f"Balance cannot be negative: {self._balance}"
            )
            assert isinstance(self._transaction_count, int), (
                "Transaction count must be integer"
            )
            assert self._transaction_count >= 0, (
                "Transaction count cannot be negative"
            )
        
        def deposit(self, amount: float):
            """Deposit money with validation."""
            assert isinstance(amount, (int, float)), (
                "Deposit amount must be numeric"
            )
            assert amount > 0, f"Deposit amount must be positive: {amount}"
            
            self._balance += amount
            self._transaction_count += 1
            
            self._check_invariants()
            print(f"✅ Deposited ${amount:.2f}. "
                  f"New balance: ${self._balance:.2f}")
        
        def withdraw(self, amount: float):
            """Withdraw money with validation."""
            assert isinstance(amount, (int, float)), (
                "Withdrawal amount must be numeric"
            )
            assert amount > 0, (
                f"Withdrawal amount must be positive: {amount}"
            )
            assert amount <= self._balance, (
                f"Insufficient funds: trying to withdraw ${amount:.2f} "
                f"but balance is ${self._balance:.2f}"
            )
            
            self._balance -= amount
            self._transaction_count += 1
            
            self._check_invariants()
            print(f"✅ Withdrew ${amount:.2f}. "
                  f"New balance: ${self._balance:.2f}")
        
        @property
        def balance(self) -> float:
            """Get current balance."""
            self._check_invariants()
            return self._balance
        
        @property
        def transaction_count(self) -> int:
            """Get transaction count."""
            return self._transaction_count
    
    # Test the bank account
    try:
        account = BankAccount("ACC-001", 100.0)
        print(f"Account created with balance: ${account.balance:.2f}")
        
        account.deposit(50.0)
        account.withdraw(30.0)
        account.deposit(25.0)
        
        print(f"Final balance: ${account.balance:.2f}")
        print(f"Total transactions: {account.transaction_count}")
        
        # This should fail
        print("\n--- Testing invalid withdrawal ---")
        account.withdraw(200.0)  # Should trigger assertion
        
    except AssertionError as e:
        print(f"✅ Correctly caught invalid operation: {e}")


def assertion_best_practices():
    """Demonstrate assertion best practices."""
    print("\n" + "="*50)
    print("🎯 ASSERTION BEST PRACTICES")
    print("="*50)
    
    practices = [
        "1. Use assertions for debugging, not for handling expected errors",
        "2. Include descriptive error messages in assertions",
        "3. Check preconditions at the start of functions",
        "4. Validate postconditions before returning",
        "5. Maintain class invariants in critical methods",
        "6. Don't use assertions for user input validation",
        "7. Remember assertions can be disabled with -O flag",
        "8. Keep assertion conditions simple and clear",
        "9. Use assertions to document assumptions",
        "10. Test both successful and failing assertions"
    ]
    
    for practice in practices:
        print(f"  {practice}")
    
    print("\n⚠️  Important: Assertions are disabled when Python runs "
          "with -O optimization flag!")
    print("   For production input validation, use explicit if statements "
          "and raise exceptions.")


if __name__ == "__main__":
    print("🔍 Python Assert Statements Tutorial")
    print("="*40)
    
    # Run all examples
    basic_assertions()
    function_preconditions()
    data_structure_validation()
    list_processing_assertions()
    class_invariant_assertions()
    assertion_best_practices()
    
    print("\n✅ Assert statements tutorial completed!")
    print("Next: Learn about logging in 03_logging_basics.py")
