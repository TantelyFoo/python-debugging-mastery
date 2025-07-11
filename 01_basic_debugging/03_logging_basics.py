"""
Python Logging Basics for Debugging

The logging module is Python's powerful built-in tool for recording events
during program execution. It's essential for debugging, monitoring, and
understanding program behavior in both development and production.
"""

import logging
import sys
from datetime import datetime
from pathlib import Path


def basic_logging_setup():
    """Demonstrate basic logging configuration and usage."""
    print("=== Basic Logging Setup ===")
    
    # Basic configuration - this should be done once at the start
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Get a logger
    logger = logging.getLogger(__name__)
    
    # Different log levels
    logger.debug("This is a debug message - detailed info for diagnosing problems")
    logger.info("This is an info message - general information about program execution")
    logger.warning("This is a warning message - something unexpected happened")
    logger.error("This is an error message - a serious problem occurred")
    logger.critical("This is a critical message - very serious error occurred")
    
    print("✅ Basic logging examples completed")


def logging_levels_demo():
    """Demonstrate different logging levels and when to use them."""
    print("\n=== Logging Levels Demo ===")
    
    # Create a custom logger
    logger = logging.getLogger("demo_logger")
    logger.setLevel(logging.DEBUG)
    
    # Create console handler with formatting
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(console_handler)
    
    # Demonstrate each level with realistic scenarios
    def process_user_registration(username, email, age):
        """Example function with comprehensive logging."""
        logger.info(f"Starting user registration for: {username}")
        
        # Debug level - detailed information for troubleshooting
        logger.debug(f"Input validation - username: {username}, "
                    f"email: {email}, age: {age}")
        
        # Validation with appropriate logging
        if not username or len(username) < 3:
            logger.error(f"Invalid username: '{username}' - must be 3+ characters")
            return False
        
        if '@' not in email:
            logger.error(f"Invalid email format: '{email}'")
            return False
        
        if age < 13:
            logger.warning(f"User {username} is under 13 years old (age: {age})")
        
        # Info level - normal program flow
        logger.info(f"User validation passed for {username}")
        
        # Simulate database operation
        try:
            # Debug level - technical details
            logger.debug(f"Attempting database insert for user {username}")
            
            # Simulate potential database error
            if username == "error_test":
                raise ConnectionError("Database connection failed")
            
            # Success
            logger.info(f"User {username} successfully registered")
            return True
            
        except ConnectionError as e:
            # Error level - serious problems
            logger.error(f"Database error during registration for {username}: {e}")
            return False
        except Exception as e:
            # Critical level - unexpected errors that might crash the system
            logger.critical(f"Unexpected error during registration: {e}")
            return False
    
    # Test different scenarios
    test_users = [
        ("alice", "alice@example.com", 25),
        ("bob", "bob@test.org", 12),  # Underage warning
        ("", "invalid@email.com", 30),  # Invalid username
        ("charlie", "not-an-email", 25),  # Invalid email
        ("error_test", "test@example.com", 30),  # Simulate DB error
    ]
    
    for username, email, age in test_users:
        print(f"\n--- Processing: {username} ---")
        result = process_user_registration(username, email, age)
        print(f"Result: {'Success' if result else 'Failed'}")


def file_logging_setup():
    """Demonstrate logging to files."""
    print("\n=== File Logging Setup ===")
    
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Create a logger for file output
    file_logger = logging.getLogger("file_logger")
    file_logger.setLevel(logging.DEBUG)
    
    # File handler for all logs
    log_file = log_dir / "application.log"
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setLevel(logging.DEBUG)
    
    # Error file handler for errors only
    error_log_file = log_dir / "errors.log"
    error_handler = logging.FileHandler(error_log_file, mode='a')
    error_handler.setLevel(logging.ERROR)
    
    # Detailed formatter for files
    detailed_formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(detailed_formatter)
    error_handler.setFormatter(detailed_formatter)
    
    # Add handlers
    file_logger.addHandler(file_handler)
    file_logger.addHandler(error_handler)
    
    # Example usage
    def process_data_file(filename):
        """Example function that logs to files."""
        file_logger.info(f"Starting to process file: {filename}")
        
        try:
            # Simulate file processing
            if filename == "missing.txt":
                raise FileNotFoundError(f"File not found: {filename}")
            
            if filename == "corrupt.txt":
                raise ValueError(f"File is corrupted: {filename}")
            
            # Success case
            file_logger.debug(f"File {filename} opened successfully")
            file_logger.info(f"Processing completed for {filename}")
            return True
            
        except FileNotFoundError as e:
            file_logger.error(f"File not found error: {e}")
            return False
        except ValueError as e:
            file_logger.error(f"Data validation error: {e}")
            return False
        except Exception as e:
            file_logger.critical(f"Unexpected error processing {filename}: {e}")
            return False
    
    # Test file processing
    test_files = ["data.txt", "missing.txt", "corrupt.txt", "valid.csv"]
    
    for filename in test_files:
        result = process_data_file(filename)
        print(f"Processing {filename}: {'Success' if result else 'Failed'}")
    
    print(f"✅ Logs written to:")
    print(f"   - All logs: {log_file}")
    print(f"   - Errors only: {error_log_file}")


def conditional_logging():
    """Demonstrate conditional and parameterized logging."""
    print("\n=== Conditional and Parameterized Logging ===")
    
    # Create logger with custom configuration
    logger = logging.getLogger("conditional_logger")
    logger.setLevel(logging.DEBUG)
    
    # Console handler
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '%(levelname)s: %(message)s'
    ))
    logger.addHandler(handler)
    
    def expensive_operation_debug():
        """Simulate an expensive debug operation."""
        # This would be expensive to compute
        import time
        time.sleep(0.1)  # Simulate expensive operation
        return "Detailed debug information with complex calculations"
    
    def smart_logging_example(data, debug_mode=False):
        """Example of smart logging practices."""
        logger.info(f"Processing {len(data)} items")
        
        # Conditional expensive debugging
        if logger.isEnabledFor(logging.DEBUG):
            debug_info = expensive_operation_debug()
            logger.debug(f"Debug details: {debug_info}")
        
        # Lazy string formatting - only format if message will be logged
        for i, item in enumerate(data):
            # Good: Lazy evaluation using % formatting
            logger.debug("Processing item %d: %s", i, item)
            
            # Also good: Check level before expensive operations
            if debug_mode and logger.isEnabledFor(logging.DEBUG):
                # Only do expensive computation if debug is enabled
                item_analysis = f"Analysis: {item} has {len(str(item))} characters"
                logger.debug(item_analysis)
        
        logger.info("Processing completed successfully")
    
    # Test conditional logging
    test_data = ["apple", "banana", "cherry", "date"]
    
    print("--- Running with DEBUG level ---")
    logger.setLevel(logging.DEBUG)
    smart_logging_example(test_data, debug_mode=True)
    
    print("\n--- Running with INFO level ---")
    logger.setLevel(logging.INFO)
    smart_logging_example(test_data, debug_mode=True)


def structured_logging():
    """Demonstrate structured logging with context."""
    print("\n=== Structured Logging ===")
    
    # Custom formatter for structured logs
    class StructuredFormatter(logging.Formatter):
        def format(self, record):
            # Add custom context to log records
            if hasattr(record, 'user_id'):
                record.msg = f"[User:{record.user_id}] {record.msg}"
            if hasattr(record, 'request_id'):
                record.msg = f"[Request:{record.request_id}] {record.msg}"
            return super().format(record)
    
    # Setup structured logger
    struct_logger = logging.getLogger("structured")
    struct_logger.setLevel(logging.DEBUG)
    
    handler = logging.StreamHandler()
    handler.setFormatter(StructuredFormatter(
        '%(asctime)s | %(levelname)-8s | %(message)s',
        datefmt='%H:%M:%S'
    ))
    struct_logger.addHandler(handler)
    
    def process_user_request(user_id, request_id, action):
        """Example of structured logging with context."""
        # Create log record with extra context
        extra = {'user_id': user_id, 'request_id': request_id}
        
        struct_logger.info(f"Processing {action} request", extra=extra)
        struct_logger.debug(f"Request details: action={action}", extra=extra)
        
        try:
            # Simulate processing
            if action == "delete_account":
                struct_logger.warning("Destructive action requested", extra=extra)
            
            if action == "invalid_action":
                raise ValueError(f"Unknown action: {action}")
            
            struct_logger.info(f"Request {action} completed successfully", extra=extra)
            return True
            
        except ValueError as e:
            struct_logger.error(f"Invalid request: {e}", extra=extra)
            return False
    
    # Test structured logging
    requests = [
        ("user123", "req001", "view_profile"),
        ("user456", "req002", "update_email"),
        ("user789", "req003", "delete_account"),
        ("user101", "req004", "invalid_action"),
    ]
    
    for user_id, request_id, action in requests:
        print(f"\n--- Processing Request {request_id} ---")
        process_user_request(user_id, request_id, action)


def logging_best_practices():
    """Summary of logging best practices."""
    print("\n" + "="*50)
    print("🎯 LOGGING BEST PRACTICES")
    print("="*50)
    
    practices = [
        "1. Use appropriate log levels (DEBUG < INFO < WARNING < ERROR < CRITICAL)",
        "2. Configure logging once at application startup",
        "3. Use logger.isEnabledFor() before expensive debug operations",
        "4. Include context in log messages (user ID, request ID, etc.)",
        "5. Use structured logging for complex applications",
        "6. Log at decision points and state changes",
        "7. Don't log sensitive information (passwords, tokens, etc.)",
        "8. Use lazy string formatting with % or .format()",
        "9. Log exceptions with full stack traces using exc_info=True",
        "10. Rotate log files to manage disk space",
        "11. Use different handlers for different log levels",
        "12. Include function names and line numbers in detailed logs"
    ]
    
    for practice in practices:
        print(f"  {practice}")
    
    print("\n📝 Log Level Guidelines:")
    guidelines = {
        "DEBUG": "Detailed info for diagnosing problems",
        "INFO": "General information about program execution",
        "WARNING": "Something unexpected happened, but program continues",
        "ERROR": "Serious problem that prevented function from working",
        "CRITICAL": "Very serious error, program may not continue"
    }
    
    for level, description in guidelines.items():
        print(f"  {level:8s}: {description}")


if __name__ == "__main__":
    print("📝 Python Logging Basics Tutorial")
    print("="*40)
    
    # Run all examples
    basic_logging_setup()
    logging_levels_demo()
    file_logging_setup()
    conditional_logging()
    structured_logging()
    logging_best_practices()
    
    print("\n✅ Logging basics tutorial completed!")
    print("Next: Learn advanced logging in 04_logging_advanced.py")
