# 🐍 Advanced Python Development Techniques

<div align="center">

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   🎯 Decorators  |  ⚡ Generators  |  🔮 Metaprogramming     ║
║                                                               ║
║   🧪 Unit Testing  |  🎨 Design Patterns  |  🚀 Best Practices║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Master the art of advanced Python programming with hands-on examples**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Topics Covered](#-topics-covered)
  - [Decorators](#-decorators)
  - [Generators](#-generators)
  - [Metaprogramming](#-metaprogramming)
  - [Unit Testing](#-unit-testing)
- [Environment Setup](#-environment-setup)
- [Installation](#-installation)
- [Usage](#-usage)
- [Learning Outcomes](#-learning-outcomes)
- [Resources](#-resources)

---

## 🎓 Overview

This repository contains a comprehensive collection of **advanced Python programming techniques** learned through hands-on practice and real-world applications. The project demonstrates mastery of Python's powerful features that separate intermediate developers from advanced practitioners.

### 🌟 What Makes This Advanced?

- **Functional Programming Paradigms** - Leveraging decorators and higher-order functions
- **Memory Optimization** - Using generators for efficient data processing
- **Dynamic Code Generation** - Metaprogramming with metaclasses and the `type()` function
- **Test-Driven Development** - Building production-ready applications with comprehensive test coverage

---

## 📁 Project Structure

```
Advanced-Python/
│
├── 📄 README.md                    # This file
├── 📄 LICENSE                      # MIT License
│
└── src/
    ├── 🎨 decorator/               # Decorator patterns and applications
    │   ├── decorator_timer_demo.py       # Performance timing decorator
    │   ├── decorator_cache_demo.py       # Memoization/caching decorator
    │   ├── decorator_logging_demo.py     # Logging decorator
    │   ├── decorator_demo.md             # Comprehensive decorator guide
    │   └── test.py                       # Decorator tests
    │
    ├── ⚡ generator/                # Generator functions
    │   └── generator.py                  # Generator examples
    │
    ├── 🔮 metaprogramming/          # Metaclasses and dynamic programming
    │   └── metaprogramming_demo.py       # Dynamic class creation
    │
    └── 🧪 unit_test/                # Test-Driven Development
        └── demo/                         # Flask blog application
            ├── app.py                    # Flask API endpoints
            ├── requirements.txt          # Python dependencies
            ├── tests/                    # Comprehensive test suite
            │   ├── conftest.py          # pytest fixtures
            │   └── test_app.py          # Integration tests
            ├── templates/               # HTML templates
            └── static/                  # JavaScript and CSS
```

---

## 🎯 Topics Covered

### 🎨 Decorators

Decorators are one of Python's most powerful features, allowing you to modify or enhance functions without changing their code. This section explores practical decorator applications:

#### **📊 Timer Decorator**
Measure function execution time for performance optimization:

```python
@timer
def matrix_multiply(a, b):
    return np.array(a) @ np.array(b)

# Output: Function matrix_multiply took 0.000123s to execute.
```

#### **💾 Cache Decorator**
Implement memoization to speed up expensive computations:

```python
@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

#### **📝 Logging Decorator**
Automatically log function calls and arguments for debugging:

```python
@log_function
def process_user_data(user_id, data):
    # Processing logic here
    pass
```

**Key Concepts:**
- `*args` and `**kwargs` for flexible function signatures
- Wrapper functions and closures
- Function metadata preservation with `functools.wraps`
- Practical applications in real-world projects

---

### ⚡ Generators

Generators enable memory-efficient iteration over large datasets by yielding items one at a time instead of loading everything into memory.

**Benefits:**
- 🚀 **Memory Efficient** - Process large files without loading entire content
- ⏱️ **Lazy Evaluation** - Compute values only when needed
- ♾️ **Infinite Sequences** - Generate unlimited data streams

**Use Cases:**
- Processing large CSV files
- Reading log files line by line
- Creating data pipelines
- Implementing custom iterators

---

### 🔮 Metaprogramming

Metaprogramming is "code that writes code" - enabling dynamic class and function creation at runtime.

#### **Dynamic Class Creation**

Create user classes dynamically based on runtime requirements:

```python
def create_user_class(class_name, attributes):
    """Dynamically generates user classes with specified attributes."""
    # Implementation uses type() to create classes on the fly
    return type(class_name, (object,), class_attrs)

# Create different user types dynamically
BasicUser = create_user_class("BasicUser", ["username", "email"])
PremiumUser = create_user_class("PremiumUser", ["username", "email", "subscription_level"])
```

**Applications:**
- 🏗️ Building flexible frameworks
- 🔧 Creating Domain-Specific Languages (DSLs)
- 🤖 Automating repetitive class definitions
- 🎭 Implementing design patterns (Factory, Builder)

**Key Concepts:**
- The `type()` function as a class factory
- Metaclasses and `__new__` method
- Dynamic attribute assignment with `setattr`
- Runtime code generation

---

### 🧪 Unit Testing (TDD)

Built a complete **Flask blog application** using **Test-Driven Development** principles. This hands-on project demonstrates production-ready testing practices.

#### **🎯 Project: Intelligent Blog Application**

A full-stack web application built using TDD methodology:

**Features:**
- ✅ RESTful API with Flask
- ✅ Create and retrieve blog posts
- ✅ JSON data validation
- ✅ Comprehensive test coverage
- ✅ Beautiful responsive UI
- ✅ Error handling and status codes

**Tech Stack:**
- **Backend:** Flask 3.0.0
- **Testing:** pytest 7.4.3, pytest-mock
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)

#### **Test Coverage**

The project includes **5 comprehensive integration tests**:

1. ✅ `test_posts_initialized_as_empty_list` - Verify initial state
2. ✅ `test_get_posts` - Test GET endpoint returns empty list
3. ✅ `test_create_post` - Test successful post creation
4. ✅ `test_create_post_invalid_data` - Test validation and error handling
5. ✅ `test_create_post_mock_posts` - Test with mocked dependencies

#### **API Endpoints**

```python
GET  /          # Render home page
GET  /posts     # Get all blog posts (JSON)
POST /posts     # Create new blog post (JSON)
```

**Example Request:**
```bash
curl -X POST http://localhost:5000/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Post", "content": "Hello World!"}'
```

**Response:**
```json
{
  "id": 1,
  "title": "My First Post",
  "content": "Hello World!"
}
```

#### **TDD Workflow Demonstrated**

1. 🔴 **Red** - Write failing tests first
2. 🟢 **Green** - Write minimum code to pass tests
3. 🔵 **Refactor** - Improve code while maintaining test coverage

---

## 🛠️ Environment Setup

### Prerequisites

Ensure you have the following installed:

- **Python 3.10+** ([Download](https://www.python.org/downloads/))
- **pip** (Python package manager)
- **virtualenv** (recommended for isolated environments)

### Quick Start

```bash
# Check Python version
python --version  # Should be 3.10 or higher

# Verify pip installation
pip --version
```

---

## 💻 Installation

### 1️⃣ Clone the Repository

```bash
cd ~/Documents
git clone <repository-url>
cd Advanced-Python-Development-Techniques/Advanced-Python
```

### 2️⃣ Create Virtual Environment

Creating a virtual environment keeps your project dependencies isolated:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You should see `(venv)` prefix in your terminal.

### 3️⃣ Install Dependencies

Install required packages for different modules:

#### **For Decorator Examples:**
```bash
pip install numpy
```

#### **For Unit Testing / Flask Blog:**
```bash
cd src/unit_test/demo
pip install -r requirements.txt
```

This installs:
- Flask 3.0.0 - Web framework
- pytest 7.4.3 - Testing framework
- pytest-mock - Mocking utilities
- Werkzeug 3.0.1 - WSGI utility library

---

## 🚀 Usage

### Running Decorator Examples

```bash
# Navigate to decorator directory
cd src/decorator

# Run timer decorator demo
python decorator_timer_demo.py

# Expected output:
# Function add took 0.000002s to execute.
# result1: 4998
# Function matrix_multiply took 0.000123s to execute.
# result2: [[19 22]
#          [43 50]]

# Run cache decorator demo
python decorator_cache_demo.py

# Run logging decorator demo
python decorator_logging_demo.py
```

### Running Generator Examples

```bash
cd src/generator
python generator.py
```

### Running Metaprogramming Examples

```bash
cd src/metaprogramming
python metaprogramming_demo.py

# Output:
# Alice
# gold
```

### Running Unit Tests (Flask Blog)

```bash
# Navigate to the project
cd src/unit_test/demo

# Run all tests with verbose output
pytest tests/ -v

# Expected output:
# tests/test_app.py::test_posts_initialized_as_empty_list PASSED
# tests/test_app.py::test_get_posts PASSED
# tests/test_app.py::test_create_post PASSED
# tests/test_app.py::test_create_post_invalid_data PASSED
# tests/test_app.py::test_create_post_mock_posts PASSED
# ========== 5 passed in 0.15s ==========

# Run specific test
pytest tests/test_app.py::test_create_post -v

# Run with coverage report
pip install pytest-cov
pytest tests/ --cov=app --cov-report=html
```

### Running the Flask Blog Application

```bash
# Make sure you're in the demo directory
cd src/unit_test/demo

# Start the Flask development server
python app.py

# Output:
# * Running on http://127.0.0.1:5000
# * Debug mode: on
```

Open your browser and navigate to: **http://localhost:5000**

#### **Using the API:**

```bash
# Create a new post
curl -X POST http://localhost:5000/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "Advanced Python", "content": "Learning decorators!"}'

# Get all posts
curl http://localhost:5000/posts

# Test error handling (invalid data)
curl -X POST http://localhost:5000/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "Missing content"}'
```

---

## 🎓 Learning Outcomes

By completing this project, I have gained expertise in:

### 🎨 **Decorators**
- ✅ Understanding closures and higher-order functions
- ✅ Creating custom decorators for cross-cutting concerns
- ✅ Using `*args`, `**kwargs` for flexible function signatures
- ✅ Preserving function metadata with `functools.wraps`
- ✅ Practical applications: timing, caching, logging, authentication

### ⚡ **Generators**
- ✅ Memory-efficient data processing
- ✅ Lazy evaluation and on-demand computation
- ✅ Creating custom iterators with `yield`
- ✅ Generator expressions and comprehensions
- ✅ Use cases for large file processing

### 🔮 **Metaprogramming**
- ✅ Dynamic class creation using `type()`
- ✅ Understanding metaclasses and `__new__`
- ✅ Runtime attribute manipulation
- ✅ Building flexible, adaptable frameworks
- ✅ Knowing when (and when not) to use metaprogramming

### 🧪 **Test-Driven Development**
- ✅ Writing tests before implementation (Red-Green-Refactor)
- ✅ Using pytest for Python testing
- ✅ Creating fixtures and test configurations
- ✅ Integration testing for web applications
- ✅ Mocking dependencies for isolated testing
- ✅ Writing maintainable, well-tested code

### 🌐 **Web Development**
- ✅ Building RESTful APIs with Flask
- ✅ Handling JSON requests and responses
- ✅ HTTP status codes and error handling
- ✅ Request validation and data sanitization
- ✅ Full-stack development (Backend + Frontend)

---

## 📖 Resources

### Official Documentation
- [Python Decorators](https://docs.python.org/3/glossary.html#term-decorator) 📚
- [Python Generators](https://docs.python.org/3/howto/functional.html#generators) ⚡
- [Python Metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses) 🔮
- [pytest Documentation](https://docs.pytest.org/) 🧪
- [Flask Documentation](https://flask.palletsprojects.com/) 🌐

### Recommended Reading
- *Fluent Python* by Luciano Ramalho
- *Python Cookbook* by David Beazley
- *Effective Python* by Brett Slatkin
- *Test-Driven Development with Python* by Harry Percival

---

## 🏆 Key Takeaways

> **"Simple is better than complex. Complex is better than complicated."**  
> — The Zen of Python

### What I Learned:

1. **Decorators are powerful** - They enable clean separation of concerns and code reusability
2. **Generators save memory** - Essential for processing large datasets efficiently
3. **Metaprogramming is a superpower** - Use responsibly to create elegant solutions
4. **Tests provide confidence** - TDD ensures code quality and catches bugs early
5. **Python is expressive** - Advanced features enable writing elegant, maintainable code

---

## 🤝 Contributing

Feel free to explore, learn, and build upon this project! If you have suggestions or improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

Special thanks to:
- **Coursera** for the Advanced Python Development course
- **Python Software Foundation** for creating an amazing language
- The **open-source community** for continuous inspiration

---

<div align="center">

**🐍 Happy Pythoning! 🐍**

Made with ❤️ and lots of ☕

*"Code is like humor. When you have to explain it, it's bad."* – Cory House

</div>
