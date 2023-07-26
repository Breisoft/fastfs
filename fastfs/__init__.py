from typing import Any, Union, List, Tuple, Dict

from fastfs.global_instance import fast_file_manager


def write_pickle(file_name: str, file_data: Any):
    """
    Writes data to a pickle file.

    Args:
        file_name: The name/path of the file to write the pickle data to.
        file_data: The data to write as a pickle object.
    """
    fast_file_manager.write_pickle(file_name, file_data)


def write_json(file_name: str, file_data: Any):
    """
    Writes data to a JSON file.

    Args:
        file_name: The name/path of the file to write the JSON data to.
        file_data: The data to write as a JSON object.
    """
    fast_file_manager.write_json(file_name, file_data)


def write_csv(file_name: str, file_data: Union[List[dict], List[list]], header: Union[None, list] = None):
    """
    Writes data to a CSV file.

    Args:
        file_name: The name/path of the file to write the CSV data to.
        file_data: The data to write as a list of dictionaries or a list of lists.
        header: An optional list of header values. If provided, this will be written as the first row in the CSV file.
    """
    fast_file_manager.write_csv(file_name, file_data, header=header)


def read_csv(file_name: str, return_list_of_dicts: bool = False) -> Union[Tuple[List[str], List[List[str]]], List[dict]]:
    """
    Reads data from a CSV file.

    Args:
        file_name: The name/path of the CSV file to read from.

    Returns:
        Union[Tuple[List[str], List[List[str]]], List[dict]]: The data read from the CSV file, either a tuple containing headers and rows 
        or a single list of dicts with the headers as the keys in the list.
    """

    return fast_file_manager.read_csv(file_name, return_list_of_dicts=return_list_of_dicts)


def write_file(file_name: str, file_data: Any):
    """
    Writes data to a file.

    Args:
        file_name: The name/path of the file to write the data to.
        file_data: The data to write to the file.
    """
    fast_file_manager.write_file(file_name, file_data)


def read_pickle(file_name: str) -> Any:
    """
    Reads data from a pickle file.

    Args:
        file_name: The name/path of the pickle file to read from.

    Returns:
        Any: The data read from the pickle file.
    """
    return fast_file_manager.read_pickle(file_name)


def read_json(file_name: str) -> Union[dict, list]:
    """
    Reads data from a JSON file.

    Args:
        file_name: The name/path of the JSON file to read from.

    Returns:
        Union[dict, list]: The data read from the JSON file, either a dictionary or a list.
    """
    return fast_file_manager.read_json(file_name)


def read_file(file_name: str) -> str:
    """
    Reads data from a file.

    Args:
        file_name: The name/path of the file to read from.

    Returns:
        str: The data read from the file.
    """
    return fast_file_manager.read_file(file_name)


def write_lines(file_name: str, lines: list):
    """
    Writes a list of lines to a file.

    Args:
        file_name: The name/path of the file to write the lines to.
        lines: A list of strings to write to the file, one string per line.
    """
    fast_file_manager.write_lines(file_name, lines)


def read_lines(file_name: str) -> List[str]:
    """
    Reads lines from a file.

    Args:
        file_name: The name/path of the file to read lines from.

    Returns:
        List[str]: A list of strings containing the lines read from the file.
    """
    return fast_file_manager.read_lines(file_name)


def write_ini(file_name: str, data: Union[Dict[Any, Dict[Any, Any]], Dict[Any, Any]]):
    """
    Writes data to an INI file.

    Args:
        file_name: The name/path of the file to write the data to.
        data: The data to write to the INI file. It can either be a dict or a dict of dicts.
        If data is only a dict, the data will be written to under the 'DEFAULT' section.
    """
    fast_file_manager.write_ini(file_name, data)


def read_ini(file_name: str) -> Union[Dict[Any, Dict[Any, Any]], Dict[Any, Any]]:
    """
    Reads data from an INI file.

    Args:
        file_name: The name/path of the INI file to read from.

    Returns:
        Union[Dict[Any, Dict[Any, Any]], Dict[Any, Any]]: The data read from the INI file. 
        If the INI file has multiple sections, it returns a dict of dicts. If it only has a default section, it returns a flat dict.
    """
    return fast_file_manager.read_ini(file_name)
