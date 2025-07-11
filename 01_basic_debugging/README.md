# Phase 1: Basic Debugging Techniques

## 🎯 Learning Objectives

By the end of this phase, you will:
- Master strategic print() statement placement for effective debugging
- Understand and implement assert statements for validation
- Configure and use Python's logging module appropriately
- Develop systematic approaches to identifying and fixing bugs

## 📋 Skills Checklist

- [ ] Strategic print debugging
- [ ] Assert statement implementation
- [ ] Logging configuration and usage
- [ ] Basic error identification
- [ ] Debug output analysis

## 🛠 Core Concepts

### 1. Print Statement Debugging
**When to use:** Quick inspection of variable values and program flow

**Best Practices:**
- Use descriptive labels with print statements
- Include context information (function name, line number)
- Use f-strings for formatted output
- Remove debug prints before production

### 2. Assert Statements
**When to use:** Validating assumptions and preconditions

**Best Practices:**
- Include meaningful error messages
- Use for internal consistency checks
- Avoid for user input validation
- Keep assertions simple and clear

### 3. Logging Module
**When to use:** Persistent debugging information and application monitoring

**Best Practices:**
- Use appropriate log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Configure loggers properly
- Include context in log messages
- Use structured logging for complex applications

## 📚 Learning Materials

### Required Reading
1. `01_print_debugging.py` - Print statement strategies
2. `02_assert_statements.py` - Assertion-based debugging
3. `03_logging_basics.py` - Logging fundamentals
4. `04_logging_advanced.py` - Advanced logging techniques

### Exercises
1. `exercise_01_bug_hunt.py` - Find and fix bugs using print statements
2. `exercise_02_assertions.py` - Add assertions to validate code
3. `exercise_03_logging_setup.py` - Configure logging for an application

## ⏱ Time Allocation

- **Day 1-2:** Print debugging mastery
- **Day 3-4:** Assert statements
- **Day 5-7:** Logging basics
- **Day 8-10:** Logging advanced features
- **Day 11-14:** Practice exercises and review

## 🎓 Assessment Criteria

You've mastered Phase 1 when you can:
- Quickly identify appropriate debugging technique for any scenario
- Write effective debug output that aids problem resolution
- Configure logging for different environments (dev, staging, prod)
- Debug simple programs using only basic techniques

## ➡️ Next Phase Preview

Phase 2 will introduce you to the Python debugger (pdb), where you'll learn to:
- Set interactive breakpoints
- Step through code execution
- Inspect variables in real-time
- Navigate call stacks

---

**Start with:** `01_print_debugging.py`
