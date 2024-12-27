import time
import functools
import psutil
import os

def performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        start_memory = process.memory_info().rss / 1024 / 1024  # Convert to MB
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        end_memory = process.memory_info().rss / 1024 / 1024  # Convert to MB
        memory_used = end_memory - start_memory

        # print(f"\nPerformance of {func.__name__}():")
        print(f"[[ CPU {execution_time:.4f} sec | Mem {memory_used:.2f} MB ]]")

        return result

    return wrapper
