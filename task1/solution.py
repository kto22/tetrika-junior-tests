import inspect
from functools import wraps

def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        annotations = func.__annotations__
        
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        for param_name, param_value in bound_args.arguments.items():
            if param_name in annotations:
                expected_type = annotations[param_name]
                if not isinstance(param_value, expected_type):
                    raise TypeError(f"Argument {param_name} must be of type {expected_type.__name__}")
        
        return func(*args, **kwargs)
    return wrapper 