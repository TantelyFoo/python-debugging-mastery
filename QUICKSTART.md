# 🚀 Quick Start Guide - Python Debugging Mastery

Get started with your Python debugging journey in just 15 minutes!

## ⚡ Immediate Setup (5 minutes)

### 1. Environment Setup
```powershell
# Navigate to the project directory
cd python_debugging

# Run the setup script
python setup.py

# Activate virtual environment
debugging_env\Scripts\activate

# Test the environment
python test_environment.py
```

### 2. Open in VS Code
```powershell
code .
```

## 📚 Your First Debugging Session (10 minutes)

### Start with Print Debugging
1. Open `01_basic_debugging/01_print_debugging.py`
2. Run the file: `F5` or `python 01_print_debugging.py`
3. Observe the different debugging techniques demonstrated

### Try Your First Exercise
1. Open `exercises/exercise_01_bug_hunt.py`
2. Run it to see the failing tests
3. Add print statements to debug the issues
4. Fix the bugs and verify all tests pass

### Example Debug Session:
```python
def calculate_grade(score):
    """Add debug prints to understand the logic flow."""
    print(f"🐛 calculate_grade called with score: {score}")
    
    if score >= 90:
        print("🐛 Returning grade A")
        return 'A'
    elif score >= 80:
        print("🐛 Returning grade B")
        return 'B'
    # ... continue debugging
```

## 🎯 Today's Learning Goals

By the end of today, you should:
- [ ] Understand strategic print statement placement
- [ ] Know when and how to use assert statements
- [ ] Have basic logging configured and working
- [ ] Successfully debug and fix at least 2 bugs in the exercises

## 📖 Learning Path Overview

### Week 1-2: Foundation
- **Days 1-3**: Print debugging and assertions
- **Days 4-7**: Logging basics and advanced techniques
- **Daily Practice**: 30-60 minutes of exercises

### Week 3-4: Interactive Debugging
- **Days 8-10**: Python debugger (pdb) basics
- **Days 11-14**: Advanced pdb techniques and workflows

### Week 5-6: Visual Debugging
- **Days 15-17**: VS Code debugging features
- **Days 18-21**: Multi-file and complex project debugging

### Week 7-12: Advanced Topics
- **Weeks 7-8**: Exception handling and error strategies
- **Weeks 9-10**: Performance profiling and optimization
- **Weeks 11-12**: Best practices and team workflows

## 🤖 Copilot Chat Starter Questions

Try these questions to get helpful debugging guidance:

### For Beginners:
```
"I'm new to Python debugging. Can you explain the difference between 
print statements, logging, and using a debugger? When should I use each?"
```

### For Your First Bug:
```
"I have a function that should calculate averages but it's returning 
wrong results. Can you help me add debugging statements to track down 
the issue? Here's my code: [paste code]"
```

### For Learning Strategies:
```
"I'm starting a Python debugging course. What are the most important 
debugging skills I should focus on first?"
```

## 📝 Progress Tracking

Update your progress in `PROGRESS.md` as you complete each section:

- [x] Environment setup completed
- [x] First debugging session completed
- [ ] Print debugging mastery
- [ ] Assert statements understanding
- [ ] Logging configuration
- [ ] Exercise 1 completed

## 🆘 Quick Help

### Common Issues:

**Virtual Environment Not Activating:**
```powershell
# Try the full path
C:\path\to\python_debugging\debugging_env\Scripts\activate
```

**Import Errors:**
```python
# Make sure you're in the virtual environment
pip list  # Should show installed packages
```

**VS Code Not Finding Python:**
- Press `Ctrl+Shift+P`
- Type "Python: Select Interpreter"
- Choose the virtual environment Python

### Getting Unstuck:

1. **Check the README.md** for detailed explanations
2. **Look at COPILOT_GUIDE.md** for help asking the right questions
3. **Run the test script** to verify your environment
4. **Start with simpler examples** if exercises feel too complex

## 🎉 Celebrate Your Progress!

After your first session:
- ✅ You've set up a professional debugging environment
- ✅ You've learned fundamental debugging techniques
- ✅ You've successfully debugged and fixed real code issues
- ✅ You're ready to tackle more advanced debugging challenges

## 🔄 Daily Routine Recommendation

### Morning Warm-up (15 minutes)
- Review yesterday's concepts
- Run through one debugging exercise

### Core Learning (45-60 minutes)
- Work through new material
- Practice with provided examples
- Complete exercises

### Evening Reflection (10 minutes)
- Update progress tracker
- Note challenges and insights
- Plan tomorrow's focus

---

**Ready to become a Python debugging expert? Start with Phase 1!**

```powershell
cd 01_basic_debugging
python 01_print_debugging.py
```
