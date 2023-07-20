# Utils
from typing import Callable, Any, List, Union
from fastfs.file_managers.fast_file_manager import fast_file_manager
from fastfs.types import FileTypes

def get_fs_directory(absolute_path: bool = False):

    return fast_file_manager.get_fs_directory(absolute_path=absolute_path)

def ls(directory_name: str) -> List[str]:
    return fast_file_manager.ls(directory_name)

def sort_ls(directory_name: str, sort_by: Callable[[str], Any], reverse: bool=False) -> List[str]:
    return fast_file_manager.sort_ls(directory_name, sort_by, reverse=reverse)

def file_exists(file_name: str) -> bool:
    return fast_file_manager.file_exists(file_name)

def touch_file(file_name: str):
    return fast_file_manager.touch_file(file_name)

def delete_file(file_name: str):
    fast_file_manager.delete_file(file_name)

def delete_directory(directory_name: str):
    fast_file_manager.delete_directory(directory_name)

def touch_directory(directory_name: str):
    fast_file_manager.touch_directory(directory_name)

def get_directory_info(directory_name: str):

    return fast_file_manager.get_directory_info(directory_name)

def get_file_info(file_name: str):

    return fast_file_manager.get_file_info(file_name)

def bulk_write_directory(directory_name: str, file_data_ls: List[Any], data_type: Union[FileTypes, str],
                              file_prefix: Union[None, str]=None):
    
    fast_file_manager.bulk_write_directory(directory_name, file_data_ls, data_type, file_prefix=file_prefix)

def bulk_read_directory(directory_name: str, skip_unsupported_data_type: bool=False, 
                            sort_by: Callable=None, sort_reverse=False, 
                            file_prefix: Union[None, str]=None, include_file_names: bool=False) -> List[Any]:
    
    return fast_file_manager.bulk_read_directory(directory_name, skip_unsupported_data_type=skip_unsupported_data_type,
                                                 sort_by=sort_by, sort_reverse=sort_reverse, file_prefix=file_prefix, 
                                                 include_file_names=include_file_names)