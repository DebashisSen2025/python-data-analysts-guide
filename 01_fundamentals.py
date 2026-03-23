"""
Complete Python Guide for Data Analysts
Chapter 2: Python Fundamentals
Author: Debashis Sen
"""

# ============================================================================
# 1. VARIABLES AND DATA TYPES
# ============================================================================

# Creating variables with different data types
name = "Debashis"           # String
age = 25                    # Integer
salary = 75000.50          # Float
is_analyst = True          # Boolean
skills = ["Python", "SQL"] # List

# Checking data types
print(f"Type of name: {type(name)}")      # <class 'str'>
print(f"Type of age: {type(age)}")        # <class 'int'>
print(f"Type of salary: {type(salary)}")  # <class 'float'>
print(f"Type of is_analyst: {type(is_analyst)}")  # <class 'bool'>

# Type conversion (casting)
age_string = str(age)                    # Convert to string
salary_int = int(salary)                 # Convert to int (loses decimal)
print(f"Age as string: {age_string}")     # "25"
print(f"Salary as int: {salary_int}")     # 75000

# ============================================================================
# 2. ARITHMETIC OPERATORS
# ============================================================================

a, b = 10, 3

print(f"\nArithmetic Operations:")
print(f"{a} + {b} = {a + b}")              # 13
print(f"{a} - {b} = {a - b}")              # 7
print(f"{a} * {b} = {a * b}")              # 30
print(f"{a} / {b} = {a / b:.2f}")          # 3.33
print(f"{a} // {b} = {a // b}")            # 3 (floor division)
print(f"{a} % {b} = {a % b}")              # 1 (modulus/remainder)
print(f"{a} ** {b} = {a ** b}")            # 1000 (exponentiation)

# ============================================================================
# 3. COMPARISON OPERATORS
# ============================================================================

print(f"\nComparison Operations:")
print(f"{a} > {b}: {a > b}")              # True
print(f"{a} < {b}: {a < b}")              # False
print(f"{a} == {b}: {a == b}")            # False
print(f"{a} != {b}: {a != b}")            # True
print(f"{a} >= {b}: {a >= b}")            # True
print(f"{a} <= {b}: {a <= b}")            # False

# ============================================================================
# 4. LOGICAL OPERATORS
# ============================================================================

print(f"\nLogical Operations:")
x, y = 20, 30

# AND operator
print(f"({x} > 15) and ({y} > 25): {(x > 15) and (y > 25)}")  # True

# OR operator
print(f"({x} < 15) or ({y} > 25): {(x < 15) or (y > 25)}")    # True

# NOT operator
print(f"not ({x} > 25): {not (x > 25)}")  # True

# ============================================================================
# 5. ASSIGNMENT OPERATORS
# ============================================================================

print(f"\nAssignment Operators:")
value = 100
print(f"Initial value: {value}")

value += 25
print(f"After += 25: {value}")             # 125

value -= 50
print(f"After -= 50: {value}")             # 75

value *= 2
print(f"After *= 2: {value}")              # 150

value /= 3
print(f"After /= 3: {value:.2f}")          # 50.00

# ============================================================================
# 6. STRING OPERATIONS
# ============================================================================

print(f"\nString Operations:")

name = "Debashis"
department = "Data Analytics"

# String concatenation
message = name + " works in " + department
print(f"Concatenation: {message}")

# String formatting (f-strings) - RECOMMENDED
info = f"Name: {name}, Department: {department}"
print(f"F-string formatting: {info}")

# String formatting (format method)
template = "Employee: {}, Salary: ${:,.2f}".format("Alice", 75000)
print(f"Format method: {template}")

# String methods
print(f"Length: {len(name)}")               # 8
print(f"Uppercase: {name.upper()}")         # DEBASHIS
print(f"Lowercase: {name.lower()}")         # debashis
print(f"Capitalize: {name.capitalize()}")   # Debashis
print(f"Count 's': {name.count('s')}")      # 2

# String slicing
text = "Data Analyst"
print(f"First 4 chars: {text[:4]}")         # Data
print(f"Last 7 chars: {text[-7:]}")         # Analyst
print(f"Every 2nd char: {text[::2]}")       # DtAaayt

# ============================================================================
# 7. CONSTANTS AND NAMING CONVENTIONS
# ============================================================================

# Constants (by convention, all uppercase)
PI = 3.14159
MAX_SALARY = 150000
MIN_AGE = 18

# Good variable naming
customer_name = "Alice"                    # snake_case
customer_age = 30
is_active_customer = True

# Class naming (PascalCase)
class DataAnalyst:
    """Represents a data analyst"""
    pass

# Function naming (snake_case)
def calculate_bonus(salary, rate=0.1):
    """Calculate bonus based on salary"""
    return salary * rate

# ============================================================================
# 8. PRACTICAL EXAMPLE: EMPLOYEE SALARY CALCULATION
# ============================================================================

print("\n" + "="*60)
print("EMPLOYEE SALARY CALCULATION")
print("="*60)

# Employee information
emp_name = "Alice Johnson"
emp_department = "Data Analytics"
base_salary = 75000.00
years_experience = 5
performance_rating = 4.5  # Out of 5

# Calculate various components
experience_bonus = base_salary * (years_experience / 100)  # 1% per year
performance_bonus = base_salary * (performance_rating / 10)  # 10% at 5 rating
total_bonus = experience_bonus + performance_bonus
total_salary = base_salary + total_bonus
tax_rate = 0.20
take_home = total_salary * (1 - tax_rate)

# Display results
print(f"\nEmployee: {emp_name}")
print(f"Department: {emp_department}")
print(f"Base Salary: ${base_salary:,.2f}")
print(f"Experience Bonus: ${experience_bonus:,.2f}")
print(f"Performance Bonus: ${performance_bonus:,.2f}")
print(f"Total Bonus: ${total_bonus:,.2f}")
print(f"Gross Salary: ${total_salary:,.2f}")
print(f"Tax (20%): ${total_salary * tax_rate:,.2f}")
print(f"Take Home Salary: ${take_home:,.2f}")

# ============================================================================
# 9. OPERATOR PRECEDENCE
# ============================================================================

print("\n" + "="*60)
print("OPERATOR PRECEDENCE")
print("="*60)

# Same result with and without parentheses shows precedence
result1 = 2 + 3 * 4        # 14 (multiplication first)
result2 = (2 + 3) * 4      # 20 (addition first due to parentheses)

print(f"\n2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")

# Precedence order (highest to lowest):
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary plus/minus (+x, -x)
# 4. Multiplication, Division, Floor Division, Modulus (*, /, //, %)
# 5. Addition, Subtraction (+, -)
# 6. Comparison operators (<, >, <=, >=, ==, !=)
# 7. Logical NOT (not)
# 8. Logical AND (and)
# 9. Logical OR (or)

# ============================================================================
# 10. SUMMARY OF KEY CONCEPTS
# ============================================================================

print("\n" + "="*60)
print("KEY TAKEAWAYS")
print("="*60)

summary = """
1. Use meaningful variable names (snake_case for variables)
2. Python is dynamically typed - types change based on assignment
3. String formatting with f-strings is the modern approach
4. Use parentheses to make operator precedence explicit
5. Remember: / gives float, // gives integer division
6. Logical operators: 'and' returns first False or last value
                      'or' returns first True or last value
7. Always write comments for complex logic
8. Use type conversion carefully - you might lose data
"""

print(summary)
