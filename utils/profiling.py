import time
import tracemalloc
import psutil
import os
from functools import wraps

def profile_time_memory(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())

        start_rss = process.memory_info().rss
        start_time = time.perf_counter()

        tracemalloc.start()

        result = func(*args, **kwargs)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        end_time = time.perf_counter()
        end_rss = process.memory_info().rss

        print(f"[{func.__name__}]")
        print(f"  실행 시간: {(end_time - start_time) * 1000:.3f} ms")
        print(f"  Python 메모리 피크: {peak / 1024 / 1024:.2f} MB")
        print(f"  RSS 증가량: {(end_rss - start_rss) / 1024 / 1024:.2f} MB")

        return result
    return wrapper
