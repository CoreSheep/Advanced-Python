from functools import wraps
import time
import asyncio

def async_cache(ttl_seconds=300):
    """
        1. async_cache(ttl_seconds)
        2. decorator(func)
        3. wrapper(*args, **kwargs)  -- call orignal func with @wraps(func)
    """
    def decorator(func):    # decorator should be used to wrap the real wrapper
        cache = {}

        @wraps(func)
        async def wrapper(*args, **kwargs): # Must be a aysnc wrapper
            key = str(args) + str(kwargs)

            # Cache hits
            if key in cache:
                res, timestamp = cache[key]
                if time.time() - timestamp <= ttl_seconds:
                    print(f"Cache is used for {func.__name__}")
                    return res
                
            # Cache misses
            res = await func(*args, **kwargs)
            cache[key] = (res, time.time())
            return res
        return wrapper
    return decorator


@async_cache(ttl_seconds=60)
async def fetch_exchange_rate(from_currency, to_currency):
    await asyncio.sleep(2)  # Simulate API delays
    # In reality, you need to call the api to get the exchange rate
    key = str(from_currency) + "2" + str(to_currency)
    if key == "EUR2USD":
        return 1.18
    elif key == "EUR2GBP":
        return 0.88
    elif key == "GBP2USD":
        1.32
    else: 
        return 0


async def main():
    rate1 = await fetch_exchange_rate("EUR", "USD")
    print(f"Rate: {rate1}")

    rate2 = await fetch_exchange_rate("EUR", "USD")
    print(f"Rate: {rate2}")

    rate3 = await fetch_exchange_rate("EUR", "GBP")
    print(f"Rate: {rate3}")


asyncio.run(main())