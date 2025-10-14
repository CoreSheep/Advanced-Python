# Blog Application - Test-Driven Development Lab

## Objective
Practice test-driven development (TDD) by implementing a Flask blog application to pass a pre-written test suite.

## Project Structure
```
demo/
├── app.py                 # Main Flask application (INCOMPLETE - YOUR TASK)
├── requirements.txt       # Python dependencies
├── tests/
│   ├── conftest.py       # pytest configuration (complete)
│   └── test_app.py       # Integration tests (complete)
├── static/
│   └── script.js         # Frontend JavaScript (complete)
└── templates/
    └── index.html        # HTML template (complete)
```

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
# Navigate to the demo directory
cd /Users/jiufeng/Documents/25ws/Coursera/Advanced-Python-Development-Techniques/Advanced-Python/src/demo

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Your Task

Implement the missing functionality in `app.py` to make all tests pass. The file contains detailed comments explaining what each route should do.

### Required Endpoints

1. **GET /** - Render the home page (index.html)
2. **POST /api/posts** - Create a new blog post
   - Accept JSON with `title` and `content`
   - Validate both fields are present
   - Generate unique ID and timestamp
   - Return created post with status 201
   - Return error with status 400 if validation fails

3. **GET /api/posts** - Get all blog posts
   - Return posts in reverse chronological order
   - Return status 200

4. **GET /api/posts/<id>** - Get a single post by ID
   - Return the post if found (status 200)
   - Return error if not found (status 404)

## TDD Workflow

### Step 1: Run the tests (they will fail)
```bash
pytest tests/ -v
```

You should see all tests failing because `app.py` is incomplete.

### Step 2: Implement the code
Work through `app.py` and implement each route. Start with the simplest one (the home route) and work your way up.

### Step 3: Run tests again
```bash
pytest tests/ -v
```

Keep iterating until all tests pass.

### Step 4: Test the application manually
```bash
python app.py
```

Visit `http://localhost:5000` in your browser to see your blog application in action!

## Expected Test Output (When Complete)

```
tests/test_app.py::test_home_page PASSED
tests/test_app.py::test_create_post PASSED
tests/test_app.py::test_get_posts_empty PASSED
tests/test_app.py::test_get_posts_with_data PASSED
tests/test_app.py::test_create_post_missing_title PASSED
tests/test_app.py::test_create_post_missing_content PASSED
tests/test_app.py::test_get_single_post PASSED
tests/test_app.py::test_get_nonexistent_post PASSED

======== 8 passed in 0.XX s ========
```

## Hints

- Use `render_template()` to render HTML templates
- Use `request.get_json()` to get JSON data from POST requests
- Use `jsonify()` to return JSON responses
- Use `datetime.now().isoformat()` for timestamps
- Store posts in the global `posts` list
- Remember to increment `next_id` for each new post
- Think about edge cases (missing fields, invalid IDs, etc.)

## Tips

1. **Read the tests first** - They tell you exactly what the application should do
2. **Start simple** - Implement one route at a time
3. **Run tests frequently** - After each change, run the tests to see progress
4. **Use the error messages** - pytest provides helpful information about what's failing
5. **Think about HTTP status codes** - 200 (OK), 201 (Created), 400 (Bad Request), 404 (Not Found)

## Learning Outcomes

By completing this lab, you will:
- Understand the TDD workflow (Red → Green → Refactor)
- Practice writing Flask routes and handling HTTP requests
- Learn to work with JSON data in Flask
- Understand the importance of validation and error handling
- Gain experience with pytest and integration testing

Good luck! 🚀

