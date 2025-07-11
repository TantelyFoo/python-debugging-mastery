# Phase 2: Python Debugger (pdb) Mastery

## 🎯 Learning Objectives

Master the Python debugger (pdb) for interactive debugging sessions. Learn to set breakpoints, inspect variables, navigate call stacks, and control program execution flow with confidence.

## 📋 Skills You'll Develop

- [ ] **Interactive Debugging**: Navigate pdb's command-line interface
- [ ] **Breakpoint Management**: Set, modify, and remove breakpoints strategically
- [ ] **Variable Inspection**: Examine and modify variables during execution
- [ ] **Call Stack Navigation**: Understand and traverse function call hierarchies
- [ ] **Execution Control**: Step through code line by line or function by function
- [ ] **Conditional Debugging**: Set breakpoints that trigger only under specific conditions
- [ ] **Post-mortem Analysis**: Debug crashed programs using pdb

## 🛠 Core PDB Commands Reference

### Essential Commands
- `h` or `help` - Show help for commands
- `l` or `list` - Show current code context
- `n` or `next` - Execute next line (step over)
- `s` or `step` - Step into function calls
- `c` or `continue` - Continue execution
- `q` or `quit` - Quit debugger

### Breakpoint Commands
- `b <line>` - Set breakpoint at line number
- `b <function>` - Set breakpoint at function
- `b <file:line>` - Set breakpoint in specific file
- `cl` or `clear` - Clear all breakpoints
- `cl <number>` - Clear specific breakpoint

### Information Commands
- `p <variable>` - Print variable value
- `pp <variable>` - Pretty-print variable
- `w` or `where` - Show current call stack
- `u` or `up` - Move up in call stack
- `d` or `down` - Move down in call stack
- `args` - Show function arguments

## 📚 Learning Materials

### Required Study Files
1. `01_pdb_basics.py` - Introduction to pdb interface and basic commands
2. `02_pdb_commands.py` - Comprehensive command reference with examples
3. `03_pdb_advanced.py` - Advanced techniques and workflows
4. `04_post_mortem.py` - Debugging crashed programs

### Hands-on Exercises
1. `exercise_04_pdb_navigation.py` - Practice basic pdb navigation
2. `exercise_05_breakpoint_strategies.py` - Master breakpoint placement
3. `exercise_06_stack_analysis.py` - Call stack inspection and navigation
4. `exercise_07_variable_modification.py` - Runtime variable manipulation

## ⏱ Learning Timeline

### Week 3: PDB Fundamentals
- **Day 1-2**: Basic pdb commands and interface
- **Day 3-4**: Breakpoint strategies and management
- **Day 5-7**: Variable inspection and modification

### Week 4: Advanced PDB Techniques
- **Day 8-9**: Call stack navigation and analysis
- **Day 10-11**: Conditional breakpoints and advanced commands
- **Day 12-14**: Post-mortem debugging and real-world scenarios

## 🚀 Getting Started with PDB

### Method 1: Add pdb to your code
```python
import pdb

def my_function():
    x = 10
    pdb.set_trace()  # Debugger will stop here
    y = x * 2
    return y
```

### Method 2: Run script with pdb
```bash
python -m pdb myscript.py
```

### Method 3: Post-mortem debugging
```python
import pdb
import sys

def main():
    try:
        # Your code here
        pass
    except:
        pdb.post_mortem()
```

## 🎓 Assessment Milestones

### Beginner Level ✅
- Can start and navigate basic pdb sessions
- Can set and clear breakpoints
- Can inspect variable values

### Intermediate Level ✅
- Can navigate call stacks confidently
- Can set conditional breakpoints
- Can modify variables during debugging

### Advanced Level ✅
- Can debug complex multi-file applications
- Can use post-mortem debugging effectively
- Can teach pdb techniques to others

## 🔧 PDB Best Practices

### 1. Strategic Breakpoint Placement
- Set breakpoints at decision points (if/elif statements)
- Place breakpoints before and after function calls
- Use conditional breakpoints for loops

### 2. Effective Variable Inspection
- Use `pp` for complex data structures
- Check variable types with `type(variable)`
- Inspect function arguments with `args`

### 3. Call Stack Analysis
- Use `w` to understand execution context
- Navigate with `u` and `d` to see different scopes
- Check local variables at each stack level

### 4. Efficient Debugging Workflow
- Start with broad breakpoints, then narrow down
- Use `c` to skip over known-good code
- Document your debugging session findings

## 🚨 Common PDB Pitfalls

### Avoid These Mistakes:
1. **Setting too many breakpoints** - Start with fewer, strategic ones
2. **Not using the call stack** - Understanding context is crucial
3. **Forgetting to remove pdb.set_trace()** - Clean up before committing
4. **Not exploring variable state** - pdb's power is in inspection
5. **Rushing through sessions** - Take time to understand what you see

## 🤖 Copilot Chat for PDB Learning

### Effective Questions for PDB Help:

```
"I'm debugging a recursive function with pdb. How can I effectively 
use the call stack to understand the recursion depth and variable 
states at each level?"
```

```
"Show me how to set up conditional breakpoints in pdb for debugging 
a loop that processes hundreds of items. I only want to break when 
an error condition occurs."
```

```
"I have a complex data structure (nested dictionaries and lists) 
that I need to inspect in pdb. What are the best commands and 
techniques for exploring this data?"
```

## 🔗 Integration with Other Tools

### PDB + Logging
Combine pdb with logging to get the best of both worlds:
```python
import pdb
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def debug_function():
    logger.debug("Function started")
    pdb.set_trace()  # Interactive inspection
    # Continue with logged execution
```

### PDB + IDEs
While learning pdb command-line interface:
- Use VS Code's integrated terminal for pdb sessions
- Compare pdb output with VS Code's visual debugger
- Practice both approaches for different scenarios

## 📈 Progress Tracking

Mark your progress as you complete each section:

### Basic PDB Skills
- [ ] Can start pdb sessions
- [ ] Understands basic commands (n, s, c, q)
- [ ] Can set and clear breakpoints
- [ ] Can print variable values

### Intermediate PDB Skills
- [ ] Can navigate call stacks
- [ ] Can set conditional breakpoints
- [ ] Can modify variables during execution
- [ ] Can debug multi-function programs

### Advanced PDB Skills
- [ ] Can perform post-mortem debugging
- [ ] Can debug complex data structures
- [ ] Can efficiently debug large applications
- [ ] Can combine pdb with other debugging tools

---

**Ready to master interactive debugging? Start with `01_pdb_basics.py`!**
