import time
from functools import wraps

def time_measure(ndigits=2):
    """Print execution time [sec] of function/method
    - ndigits: precision after the decimal point
    """
    def outer_wrapper(func):
        # @wraps: keep docstring of "func"
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print("runtime: {sec} [sec]".format(
                sec=round(end-start, ndigits))
            )
            return result
        return inner_wrapper
    return outer_wrapper
