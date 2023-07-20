from typing import Any, Union, List, Callable

from file_managers.fast_file_manager import fast_file_manager

def write_pickle(file_name: str, file_data: Any):
    fast_file_manager.write_pickle(file_name, file_data)

def write_json(file_name: str, file_data: Any):
    fast_file_manager.write_json(file_name, file_data)

def write_csv(file_name: str, file_data: Union[List[dict], List[list]], header: Union[None, list]=None):
    fast_file_manager.write_csv(file_name, file_data, header=header)

def write_file(file_name: str, file_data: Any):
    fast_file_manager.write_file(file_name, file_data)

def read_pickle(file_name: str) -> Any:
    return fast_file_manager.read_pickle(file_name)

def read_json(file_name: str) -> Union[dict, list]:
    return fast_file_manager.read_json(file_name)

def read_file(file_name: str) -> Any:
    return fast_file_manager.read_file(file_name)

def file_exists(file_name: str) -> bool:
    return fast_file_manager.file_exists(file_name)

def touch_file(file_name: str):
    return fast_file_manager.touch_file(file_name)

def delete_file(file_name: str):
    fast_file_manager.delete_file(file_name)

def touch_directory(directory_name: str):
    fast_file_manager.touch_directory(directory_name)

def write_lines(file_name: str, lines: list) -> Any:
    fast_file_manager.write_lines(file_name, lines)

def read_lines(file_name: str) -> Any:
    return fast_file_manager.read_lines(file_name)

def get_fs_directory():

    if file_exists('.fastfs'):
        return read_file('.fastfs')

    return None

def create_fs(directory_name: str = 'files'):
    fast_file_manager.create_fs(directory_name)

def sort_ls(directory_name: str, sort_by: Callable[[str], Any], reverse: bool=False):
    return self.sort_ls(directory_name, sort_by, reverse=reverse)
