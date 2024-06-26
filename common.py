import time, os, sys

def retry(max_retries=3, wait_time=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                result = func(*args, **kwargs)
                if (result is True):
                    return
                else:
                    retries += 1
                    if (wait_time is not None):
                        time.sleep(wait_time)
            else:
                raise TimeoutError(f"Max retries of function {func.__name__} exceeded")
        return wrapper
    return decorator


def dynamic_file_path(path) -> str:
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, path)
    else:
        return path
