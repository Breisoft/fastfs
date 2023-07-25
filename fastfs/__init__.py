from typing import Any, Union, List, Callable

from fastfs.file_managers.fast_file_manager import fast_file_manager


def write_pickle(file_name: str, file_data: Any):
    """
    Writes data to a pickle file.

    Args:
        file_name: The name of the file to write the pickle data to.
        file_data: The data to write as a pickle object.
    """
    fast_file_manager.write_pickle(file_name, file_data)


def write_json(file_name: str, file_data: Any):
    """
    Writes data to a JSON file.

    Args:
        file_name: The name of the file to write the JSON data to.
        file_data: The data to write as a JSON object.
    """
    fast_file_manager.write_json(file_name, file_data)


def write_csv(file_name: str, file_data: Union[List[dict], List[list]], header: Union[None, list] = None):
    """
    Writes data to a CSV file.

    Args:
        file_name: The name of the file to write the CSV data to.
        file_data: The data to write as a list of dictionaries or a list of lists.
        header: An optional list of header values. If provided, this will be written as the first row in the CSV file.
    """
    fast_file_manager.write_csv(file_name, file_data, header=header)


def write_file(file_name: str, file_data: Any):
    """
    Writes data to a file.

    Args:
        file_name: The name of the file to write the data to.
        file_data: The data to write to the file.
    """
    fast_file_manager.write_file(file_name, file_data)


def read_pickle(file_name: str) -> Any:
    """
    Reads data from a pickle file.

    Args:
        file_name: The name of the pickle file to read from.

    Returns:
        Any: The data read from the pickle file.
    """
    return fast_file_manager.read_pickle(file_name)


def read_json(file_name: str) -> Union[dict, list]:
    """
    Reads data from a JSON file.

    Args:
        file_name: The name of the JSON file to read from.

    Returns:
        Union[dict, list]: The data read from the JSON file, either a dictionary or a list.
    """
    return fast_file_manager.read_json(file_name)


def read_file(file_name: str) -> Any:
    """
    Reads data from a file.

    Args:
        file_name: The name of the file to read from.

    Returns:
        Any: The data read from the file.
    """
    return fast_file_manager.read_file(file_name)


def write_lines(file_name: str, lines: list) -> Any:
    """
    Writes a list of lines to a file.

    Args:
        file_name: The name of the file to write the lines to.
        lines: A list of strings to write to the file, one string per line.
    """
    fast_file_manager.write_lines(file_name, lines)


def read_lines(file_name: str) -> Any:
    """
    Reads lines from a file.

    Args:
        file_name: The name/path of the file to read lines from.

    Returns:
        List[str]: A list of strings containing the lines read from the file.
    """
    return fast_file_manager.read_lines(file_name)


def create_fs(directory_name: str = 'files', active: bool = True):
    """
    Creates a new fastfs directory.

    Args:
        directory_name: The name/path of the new directory.
        active: If True, sets the new directory as the active fastfs directory.
    """
    fast_file_manager.create_fs(directory_name, active=active)


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
