from typing import Any, Union, List, Callable

from fastfs.file_managers.fast_file_manager import fast_file_manager

def write_yaml(file_name: str, data: Any):
    fast_file_manager.write_yaml(file_name, data)

def read_yaml(file_name: str) -> Any:
    return fast_file_manager.read_yaml(file_name)

def write_hdf5(file_name: str, data: Any):
    fast_file_manager.write_hdf5(file_name, data)

def read_hdf5(file_name: str) -> Any:
    return fast_file_manager.read_hdf5(file_name)

