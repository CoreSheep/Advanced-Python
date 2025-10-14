# A Practical Guide to Python Decorators

> **Audience:** Intermediate Python developers
> **Goal:** Understand what decorators are, why they’re useful, and how to design, apply, and test them safely.

---

## 1) What Is a Decorator?

A **decorator** is a callable that takes a function (or class) and returns a new callable—usually adding behavior **without modifying the original function’s source**.

Syntactic sugar:

```py
@decorator
def func(...):
    ...
# is equivalent to:
def func(...):
    ...
func = decorator(func)
```

Common uses: logging, timing, caching, retries, access control, validation, metrics, and API rate limiting.

---

## 2) The Minimal Pattern (with `functools.wraps`)

Always preserve metadata (`__name__`, docstring, signature) with `@wraps`.

```python
from functools import wraps

def log_io(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[call] {func.__name__} args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[ret ] {func.__name__} -> {result}")
        return result
    return wrapper

@log_io
def add(a, b):
    """Add two numbers."""
    return a + b
```

**Why `@wraps` matters:** keeps introspection, help text, and tooling happy.

---

## 3) Decorators with Arguments (“Three-Layer” Pattern)

When you want `@retry(times=3)`, wrap a wrapper:

```python
from functools import wraps
import time

def retry(times=3, delay=0.1):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    time.sleep(delay)
            raise last_exc
        return wrapper
    return deco

@retry(times=5, delay=0.2)
def flaky():
    ...
```

---

## 4) Class-Based Decorators (for Stateful Behavior)

Use a class if you need state (counters, configuration, caches).

```python
from functools import wraps

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0
        wraps(func)(self)  # make the instance look like func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"Hi {name}"
```

---

## 5) Decorating Methods, `@staticmethod`, `@classmethod`, and `@property`

* Methods receive `self`/`cls` normally; nothing special needed.
* Built-ins you’ll commonly use:

```python
class Example:
    @staticmethod
    def utility(x): return x

    @classmethod
    def construct(cls, x): return cls()

    def __init__(self, first, last):
        self.first, self.last = first, last

    @property
    def full_name(self):  # accessor as attribute
        return f"{self.first} {self.last}"
```

---

## 6) Asynchronous Functions

Detect coroutine functions and `await` them appropriately.

```python
import asyncio
from functools import wraps

def async_timer(func):
    if asyncio.iscoroutinefunction(func):
        @wraps(func)
        async def aw(*args, **kwargs):
            t0 = asyncio.get_event_loop().time()
            try:
                return await func(*args, **kwargs)
            finally:
                dt = asyncio.get_event_loop().time() - t0
                print(f"{func.__name__} took {dt:.4f}s")
        return aw
    else:
        @wraps(func)
        def sw(*args, **kwargs):
            return func(*args, **kwargs)
        return sw
```

---

## 7) Stacking Decorators and Order

```python
@A
@B
def f():
    ...
# Equivalent to: f = A(B(f))
# The decorator closest to the function (B) is applied first.
```

---

## 8) Type-Safe Decorators (Modern `typing`)

Use `ParamSpec` and `TypeVar` to preserve signatures:

```python
from typing import Callable, TypeVar, ParamSpec
from functools import wraps

P = ParamSpec('P')
R = TypeVar('R')

def log_io(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print("call", func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

This keeps type checkers (mypy/pyright) accurate across decorator boundaries.

---

## 9) Battle-Tested, Ready-to-Use Patterns

### 9.1 Timing

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"{func.__name__} took {time.perf_counter() - t0:.4f}s")
    return wrapper
```

### 9.2 Caching with the Standard Library

```python
from functools import lru_cache

@lru_cache(maxsize=1024)
def fib(n: int) -> int:
    if n < 2: return n
    return fib(n-1) + fib(n-2)
```

Related: `functools.cache` (Py3.9+), `functools.cached_property` (Py3.8+).

### 9.3 Validation / Precondition Checks

```python
from functools import wraps

def non_negative_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if any(isinstance(a, (int, float)) and a < 0 for a in args):
            raise ValueError("Negative arguments not allowed.")
        return func(*args, **kwargs)
    return wrapper
```

### 9.4 Authorization (Sketch)

```python
def require_role(role: str):
    def deco(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if role not in user.roles:
                raise PermissionError("Forbidden")
            return func(user, *args, **kwargs)
        return wrapper
    return deco
```

### 9.5 Retry with Backoff (Simplified)

```python
import time
from functools import wraps

def backoff_retry(times=3, base=0.1):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = base
            last = None
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last = e
                    time.sleep(delay)
                    delay *= 2
            raise last
        return wrapper
    return deco
```

---

## 10) Testing and Debugging Decorators

* **Unit-test the decorator separately** with small dummy functions.
* **Assert side effects** (logs, counters, timing calls) deterministically.
* **Mock time/sleep/network** for reliability.
* Use `inspect.signature` and `help()` to confirm `@wraps` preserved metadata.

Example test sketch (pytest-style):

```python
def test_timer_preserves_return(capsys):
    @timer
    def plus(a, b): return a + b

    assert plus(2, 3) == 5
    out = capsys.readouterr().out
    assert "plus took" in out
```

---

## 11) Performance Considerations

* Each decorator adds a call layer—**don’t over-decorate** hot code paths.
* Prefer built-ins (`lru_cache`) for optimized behavior.
* Consider **class-based** decorators for state to avoid global lookups.
* If extreme performance matters, measure with `timeit` and minimize capture in closures.

---

## 12) Best Practices Checklist

* ✅ Always use `@wraps` (or an equivalent) to preserve metadata.
* ✅ Accept `*args, **kwargs` to keep signatures flexible (or use `ParamSpec`).
* ✅ Keep decorators **pure and composable**—avoid surprising side effects.
* ✅ Make configurations explicit via **decorator factories** (`@deco(opt=...)`).
* ✅ Handle **async vs sync** appropriately; don’t block event loops.
* ✅ Provide **clear error messages** when enforcing preconditions or auth.
* ✅ Document expectations and limitations in the decorator’s docstring.
* ✅ Write **focused tests** for the decorator and at least one integrated test.

---

## 13) Quick Reference (Cheat Sheet)

* **No-arg decorator:**

  ```py
  def deco(func):
      @wraps(func)
      def wrapper(*a, **k):
          return func(*a, **k)
      return wrapper
  ```
* **Decorator with args:**

  ```py
  def deco_factory(x):
      def deco(func):
          @wraps(func)
          def wrapper(*a, **k):
              return func(*a, **k)
          return wrapper
      return deco
  ```
* **Stateful (class-based):**

  ```py
  class Deco:
      def __init__(self, func):
          wraps(func)(self)
          self.func = func
      def __call__(self, *a, **k):
          return self.func(*a, **k)
  ```
* **Type-safe:**

  ```py
  P = ParamSpec('P'); R = TypeVar('R')
  def deco(f: Callable[P, R]) -> Callable[P, R]: ...
  ```

---

## 14) When *Not* to Use a Decorator

* When a **context manager** (`with`) or an inline call wrapper is clearer.
* When the added behavior is highly specific to one call site—prefer explicit code.
* When you need **dynamic** behavior per call (pass an object instead of decorating).

---

## 15) Further Ideas

* Compose decorators for **observability**: logging + metrics + tracing.
* Package your decorators into a small internal library with tests and docs.
* Expose configuration via environment variables or DI if used across services.

---

**Summary:** Decorators are a clean, reusable way to wrap behavior around functions and methods. Prioritize clarity (`@wraps`), safe typing (`ParamSpec`), and solid tests. Start with small utilities (timing, logging, caching) and evolve toward robust, composable building blocks.
