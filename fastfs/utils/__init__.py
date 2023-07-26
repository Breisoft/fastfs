# Utils
from typing import Callable, Any, List, Union
from fastfs.global_instance import fast_file_manager
from fastfs.data_types import FileTypes


def get_fs_directory(absolute_path: bool = False) -> str:
    """
    Returns the fastfs directory.

    Args:
        absolute_path: If True, returns the absolute path of the directory.

    Returns:
        str: The fastfs directory path.
    """
    return fast_file_manager.get_fs_directory(absolute_path=absolute_path)


def ls(directory_name: str) -> List[str]:
    """
    Lists all files in the given directory.

    Args:
        directory_name: The name/path of the directory.

    Returns:
        List[str]: A list of file names in the directory.
    """
    return fast_file_manager.ls(directory_name)


def sorted_ls(directory_name: str, sort_by: Callable[[str], Any], reverse: bool = False) -> List[str]:
    """
    Lists all files in a directory, sorted based on the given sorting function.

    Args:
        directory_name: The name/path of the directory to list files from.
        sort_by: A callable function that takes a file name as input and returns a sorting key.
        reverse: If True, sorts the files in reverse order.

    Returns:
        List[str]: A list of sorted file names in the directory.
    """
    return fast_file_manager.sorted_ls(directory_name, sort_by, reverse=reverse)


def create_fs(directory_name: str = 'files', active: bool = True):
    """
    Creates a new fastfs directory.

    Args:
        directory_name: The name/path of the new directory.
        active: If True, sets the new directory as the active fastfs directory.
    """
    fast_file_manager.create_fs(directory_name, active=active)


def file_exists(file_name: str) -> bool:
    """
    Checks if a file with the given name exists.

    Args:
        file_name: The name/path of the file to check.

    Returns:
        bool: True if the file exists, otherwise False.
    """
    return fast_file_manager.file_exists(file_name)


def touch_file(file_name: str):
    """
    Creates a new, empty file with the given name.

    Args:
        file_name: The name/path of the file to create.
    """
    return fast_file_manager.touch_file(file_name)


def delete_file(file_name: str):
    """
    Deletes the file with the given name.

    Args:
        file_name: The name/path of the file to delete.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    fast_file_manager.delete_file(file_name)


def delete_directory(directory_name: str):
    """
    Deletes the directory with the given name.

    Args:
        directory_name: The name/path of the directory to delete.

    Raises:
        FileNotFoundError: If the directory does not exist.
    """
    fast_file_manager.delete_directory(directory_name)


def touch_directory(directory_name: str):
    """
    Creates a new directory with the given name.

    Args:
        directory_name: The name/path of the directory to create.
    """
    fast_file_manager.touch_directory(directory_name)


def get_directory_info(directory_name: str) -> dict:
    """
    Returns information about the given directory.

    Args:
        directory_name: The name/path of the directory.

    Returns:
        dict: A dictionary containing information about the directory, including the absolute path, number of files,
              creation time, modification time, and total size.
    """
    return fast_file_manager.get_directory_info(directory_name)


def get_file_info(file_name: str) -> dict:
    """
    Returns information about the given file.

    Args:
        file_name: The name/path of the file.

    Returns:
        dict: A dictionary containing information about the file, including the absolute path, creation time,
              modification time, size, and extension.
    """
    return fast_file_manager.get_file_info(file_name)


def bulk_write_directory(directory_name: str, file_data_ls: List[Any], data_type: Union[FileTypes, str],
                         file_prefix: Union[None, str] = None):
    """
    Writes a list of data objects to files in a directory.

    Args:
        directory_name: The name/path of the directory to write files to.
        file_data_ls: A list of data objects to write.
        data_type: The file format to use for writing data. Supported formats include JSON, CSV, Pickle, HDF5, INI,
                   YAML, and XML.
        file_prefix: An optional prefix to append to each file name. If not provided, file names will have no prefix.
    """
    fast_file_manager.bulk_write_directory(
        directory_name, file_data_ls, data_type, file_prefix=file_prefix)


def bulk_read_directory(directory_name: str, skip_unsupported_data_type: bool = False,
                        sort_by: Callable = None, sort_reverse=False,
                        file_prefix: Union[None, str] = None, include_file_names: bool = False) -> List[Any]:
    """
    Reads files from a directory. File names must be in the same style and format as bulk_write_directory.

    Args:
        directory_name: The name/path of the directory to read files from.
        skip_unsupported_data_type: If True, skips files with unsupported file types.
        sort_by: An optional callable taking a file name as input and returning a sorting key. If provided, files will
                 be sorted based on this function's return values.
        sort_reverse: If True, sorts files in reverse order according to the sort_by callable.
        file_prefix: An optional file name prefix for filtering files to read. If not provided, all files in the
                     directory will be considered.
        include_file_names: If True, returns a dictionary mapping file names to the read data objects. If False,
                            returns a list of the read data objects.

    Returns:
        List[Any]: A list of data objects read from the directory, or a dictionary mapping file names to data objects
                   if `include_file_names` is True.
    """
    return fast_file_manager.bulk_read_directory(directory_name, skip_unsupported_data_type=skip_unsupported_data_type,
                                                 sort_by=sort_by, sort_reverse=sort_reverse, file_prefix=file_prefix,
                                                 include_file_names=include_file_names)
