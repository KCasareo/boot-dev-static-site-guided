from __future__ import annotations
from functools import wraps


def log_name(prefix : str = "", description : str = "", postfix : str = ""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Running {prefix}/{func.__name__}: {description}")
            result = func(*args, **kwargs)
            if postfix != "" or postfix is not None:
                print(f"{postfix}")
            return result
        return wrapper
    return decorator
