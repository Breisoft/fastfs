
from typing import Any


def path_replace(func):
    def wrapper(self, file_path, *args, **kwargs):
        file_path = self._path_replace(file_path)
        return func(self, file_path, *args, **kwargs)
    return wrapper


def safe_write(write_mode='w'):
    def decorator(func):
        def wrapper(self, file_name: str, file_data: Any, *args, **kwargs):
            self._safe_write_func(file_name, func, file_data,
                                  write_mode, *args, **kwargs)
        return wrapper
    return decorator


def safe_read(read_mode='r', context_manager=True):
    def decorator(func):
        def wrapper(self, file_name: str, *args, **kwargs):
            return self._safe_read_func(file_name, func, read_mode, context_manager, *args, **kwargs)
        return wrapper
    return decorator
