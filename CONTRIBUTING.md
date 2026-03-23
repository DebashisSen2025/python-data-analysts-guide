# Contributing to Complete Python Guide for Data Analysts

Thank you for your interest in contributing to this project! 🎉

This guide will help you understand how to contribute effectively.

---

## 📋 Code of Conduct

- Be respectful and inclusive
- Welcome different perspectives and experiences
- Provide constructive feedback
- Report inappropriate behavior to maintainers

---

## 🚀 How to Contribute

### 1. Report Issues

Found a bug or have a suggestion? Please create an issue:

1. Go to the [Issues](https://github.com/debashisen/python-data-analysts-guide/issues) page
2. Click "New Issue"
3. Provide a clear title and description
4. Include examples and screenshots if applicable

**Issue Labels:**
- `bug`: Something isn't working
- `enhancement`: New feature request
- `documentation`: Documentation improvement
- `question`: Question about usage
- `good first issue`: Good for newcomers

### 2. Submit Pull Requests

#### Fork the Repository
```bash
# Click "Fork" button on GitHub
git clone https://github.com/your-username/python-data-analysts-guide.git
cd python-data-analysts-guide
```

#### Create a Branch
```bash
# Create a new branch for your feature
git checkout -b feature/add-new-topic
# or for bug fixes
git checkout -b fix/issue-description
```

#### Make Changes
- Follow the project's code style (see below)
- Add comments for complex code
- Update documentation if needed
- Add or update examples

#### Test Your Changes
```bash
# Run examples to ensure they work
python examples/01_fundamentals.py
python examples/02_pandas_analysis.py

# Check code quality
pylint your_file.py
black --check your_file.py
```

#### Commit and Push
```bash
# Commit with meaningful message
git commit -m "Add: Explanation of what you added or fixed"

# Push to your fork
git push origin feature/add-new-topic
```

#### Create Pull Request
1. Go to the original repository
2. Click "New Pull Request"
3. Select your branch
4. Write a clear title and description
5. Reference related issues (#123)
6. Click "Create Pull Request"

---

## 💻 Code Style Guide

### Python Code

**Follow PEP 8:**
```bash
# Use Black for formatting
pip install black
black examples/

# Check with flake8
pip install flake8
flake8 examples/
```

### File Structure
```python
"""
Module docstring explaining what the module does.
Author: Your Name
"""

# Imports (standard library first, then third-party, then local)
import os
import sys
from datetime import datetime

import pandas as pd
import numpy as np

# Constants
MAX_EMPLOYEES = 1000
DEFAULT_SALARY = 50000

# Classes
class EmployeeManager:
    """Manages employee data."""
    pass

# Functions
def calculate_bonus(salary, rate=0.1):
    """Calculate bonus amount."""
    return salary * rate

# Main execution
if __name__ == "__main__":
    pass
```

### Naming Conventions
- Variables: `snake_case` (my_variable)
- Functions: `snake_case` (my_function)
- Classes: `PascalCase` (MyClass)
- Constants: `UPPER_CASE` (MAX_VALUE)
- Private: `_leading_underscore` (_private_var)

### Comments
```python
# Good: Explains the 'why', not the 'what'
# Calculate bonus as 10% of salary for employees with 5+ years
bonus = salary * 0.1

# Bad: Obvious from code
# Multiply salary by 0.1
bonus = salary * 0.1
```

---

## 📝 Documentation

### Adding Examples

1. Create file in `examples/` folder
2. Use this template:

```python
"""
Complete Python Guide for Data Analysts
Chapter X: Topic Name
Author: Your Name
"""

# ============================================================================
# 1. SECTION TITLE
# ============================================================================

print("=" * 70)
print("1. SECTION TITLE")
print("=" * 70)

# Your code here

# ============================================================================
# Summary
# ============================================================================

print("\nKEY TAKEAWAYS:")
print("- Point 1")
print("- Point 2")
```

### Updating README

1. Edit `README.md` clearly
2. Keep sections organized
3. Update Table of Contents if needed
4. Add links to related content

### Adding to PDF Guide

Contact the maintainer to include your contributions in the PDF guide.

---

## 🔍 Code Review Process

Our team will:
1. ✅ Review your code
2. ✅ Check for quality issues
3. ✅ Test your examples
4. ✅ Request changes if needed
5. ✅ Merge when approved

**Tips for passing review:**
- Write clear, meaningful commit messages
- Include docstrings for functions
- Add comments for complex logic
- Test your code before submitting
- Follow the style guide

---

## 📚 Types of Contributions

### 1. Code Examples
- Add new examples in `examples/` folder
- Include clear comments
- Test thoroughly

### 2. Bug Fixes
- Fix issues found in the guide
- Include before/after examples
- Update relevant documentation

### 3. Documentation
- Improve clarity
- Fix typos
- Add missing information
- Update examples

### 4. New Topics
- Suggest new chapters
- Provide draft content
- Include code examples
- Follow the guide's structure

### 5. Translations
- Translate guide to other languages
- Submit as separate branch
- Follow original structure

---

## 🎯 What We're Looking For

### High Priority
- Bug fixes
- Code examples with real-world applications
- Interview question solutions
- Performance optimization tips
- Database integration examples

### Medium Priority
- Clarifications to existing content
- Additional practice problems
- Related resources
- Visualizations and diagrams

### Lower Priority
- Minor typo fixes
- Style improvements
- Code refactoring

---

## ⚙️ Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/yourusername/python-data-analysts-guide.git
cd python-data-analysts-guide

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development tools
pip install black flake8 pylint pytest

# Verify setup
python examples/01_fundamentals.py
```

---

## 📞 Getting Help

- **Questions?** Create an issue with label `question`
- **Chat?** Join our Discord community (link in README)
- **Direct contact?** Email: debashis.sen@email.com

---

## ✨ Recognition

Contributors are recognized in:
- README.md Contributors section
- Project documentation
- GitHub contributor graphs
- Special mentions in updates

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 🙏 Thank You!

Your contributions make this guide better for everyone. We appreciate your help in making Python learning accessible to data analysts worldwide!

**Happy Contributing!** 🚀

---

<div align="center">

**Have questions? Feel free to open an issue or reach out!**

Made with ❤️ by the Python Data Analytics Community

</div>
