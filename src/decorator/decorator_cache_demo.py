from functools import lru_cache

@lru_cache(maxsize=1024)
def fibonacci(n):
	"""
    Calculates the nth Fibonacci number.
        lru_cache: Least Recently Used cache.
        @param n: The nth Fibonacci number to calculate.
        @param maxsize: The maximum number of results to cache.
        @return: The nth Fibonacci number.
    """

	if n < 2:
		return n
	return fibonacci(n-1) + fibonacci(n-2)


# Calculate the 35th Fibonacci number
print (fibonacci(35))

"""
Caching is like having a cheat sheet for your function. It stores the results of previous calculations, 
and if the function is called again with the same inputs, it simply retrieves the answer from the cache 
instead of recalculating it. This can significantly speed up your code, especially for functions 
with repetitive calculations.  
"""