from typing import Any, Union, List, Callable

from fastfs.file_managers.fast_file_manager import fast_file_manager


def write_yaml(file_name: str, data: Any):
    """
    Writes data to a YAML file.

    Args:
        file_name: The name/path of the file to write the YAML data to.
        data: The data to write as a YAML object.
    """
    fast_file_manager.write_yaml(file_name, data)


def read_yaml(file_name: str) -> Any:
    """
    Reads data from a YAML file.

    Args:
        file_name: The name/path of the YAML file to read from.

    Returns:
        Any: The data read from the YAML file.
    """
    return fast_file_manager.read_yaml(file_name)


def write_hdf5(file_name: str, data: Any):
    """
    Writes data to an HDF5 file.

    Args:
        file_name: The name/path of the file to write the HDF5 data to.
        data: The data to write as an HDF5 object.
    """
    fast_file_manager.write_hdf5(file_name, data)


def read_hdf5(file_name: str) -> Any:
    """
    Reads data from an HDF5 file.

    Args:
        file_name: The name/path of the HDF5 file to read from.

    Returns:
        Any: The data read from the HDF5 file.
    """
    return fast_file_manager.read_hdf5(file_name)


