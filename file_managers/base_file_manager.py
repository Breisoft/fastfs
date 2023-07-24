import os

from typing import Any, Callable, Union, List

import traceback
import shutil
import configparser


def path_replace(func):
    def wrapper(self, file_path, *args, **kwargs):
        file_path = self._path_replace(file_path)
        return func(self, file_path, *args, **kwargs)
    return wrapper


def safe_write(write_mode='w'):
    def decorator(func):
        def wrapper(self, file_name: str, file_data: Any, *args, **kwargs):
            self._safe_write_func(func, file_name, file_data,
                                  write_mode, *args, **kwargs)
        return wrapper
    return decorator


def safe_read(read_mode='r', context_manager=True):
    def decorator(func):
        def wrapper(self, file_name: str, *args, **kwargs):
            return self._safe_read_func(func, file_name, read_mode, context_manager, *args, **kwargs)
        return wrapper
    return decorator


class BaseFileManager():
    def __init__(self):
        self._local_fs = None

        self._fs_active = False

    def _read_local_fs(self):
        if not os.path.exists('.fastfs'):
            return None

        fast_fs_config = self.read_ini('.fastfs')

        local_fs = fast_fs_config['fastfs_directory']
        fs_active = fast_fs_config['fastfs_active']

        return local_fs, fs_active

    @property
    def local_fs(self):
        if self._local_fs is None:
            self._local_fs, self._fs_active = self._read_local_fs()
        return self._local_fs

    def _path_replace(self, file_path: str) -> str:

        # If fastfs
        if not self._fs_active:
            return file_path

        if file_path == '.fastfs':
            return file_path

        if self.local_fs is None:
            return file_path

        if os.path.isabs(file_path):
            return file_path

        if not file_path.startswith(os.path.join('.', self.local_fs)):
            return os.path.join('.', self.local_fs, file_path)

        return file_path

    def create_fs(self, directory_name: str, active: bool = True):

        self.touch_directory(directory_name)

        config = {'DEFAULT': {
            'fastfs_directory': directory_name, 'fastfs_active': active}}

        self.write_ini('.fastfs', config)
        self._local_fs = directory_name
        self._fs_active = active

    ####################################
    #         Basic file logic         #
    ####################################

    def _safe_write_func(self, func: Callable, file_name: str, file_data: Any, write_mode='w', encoding='utf-8', *args, **kwargs):
        file_name = self._path_replace(file_name)

        # Open the file in write mode
        with open(file_name, write_mode, encoding=encoding) as file:
            # Call the decorated function
            func(self, file, file_data, *args, **kwargs)

    def _safe_read_func(self, func: Callable, file_name: str, read_mode='r', context_manager=True, encoding='utf-8', *args, **kwargs):
        file_name = self._path_replace(file_name)

        if context_manager:
            with open(file_name, read_mode, encoding=encoding) as file:
                # Call the decorated function
                return func(self, file, *args, **kwargs)

        else:
            file = open(file_name, read_mode, encoding=encoding)

            return func(self, file, *args, **kwargs)

    @path_replace
    def is_hidden_file(self, file_name):
        name = os.path.basename(os.path.abspath(file_name))
        return name.startswith('.')

    @path_replace
    def touch_directory(self, directory_name: str):

        if not self.file_exists(directory_name):
            os.mkdir(directory_name)

    @path_replace
    def file_exists(self, file_name: str) -> bool:
        return os.path.exists(file_name)

    def get_fs_directory(self, absolute_path=False):
        if self.file_exists('.fastfs'):
            path = self.read_file('.fastfs')

            if absolute_path:
                path = os.path.abspath(path)

            return path

        return None

    @path_replace
    def delete_file(self, file_name: str):
        os.remove(file_name)

    @path_replace
    def delete_directory(self, directory_name: str):
        shutil.rmtree(directory_name)

    @path_replace
    def ls(self, directory: str, show_hidden=False):

        files = os.listdir(directory)

        if show_hidden:
            return files
        else:
            return [file for file in files if not self.is_hidden_file(file)]

    def _remove_extension(self, file_name):
        root, ext = os.path.splitext(file_name)
        if ext == '':
            return file_name
        return root

    def sorted_ls(self, directory: str, sort_by: Callable[[str], Any], reverse: bool = False) -> List[str]:

        ls = self.ls(directory)

        return sorted(ls, key=sort_by, reverse=reverse)

    ####################################
    #   Actual implementations below   #
    ####################################

    @safe_write()
    def write_file(self, file, file_data):
        if not isinstance(file_data, str):
            file_data = str(file_data)

        file.write(file_data)

    @safe_read()
    def read_file(self, file):
        return file.read()

    @safe_write()
    def touch_file(self, file_name: str):
        if not self.file_exists(file_name):
            self.write_file(file_name, '')

    # We only include read/write ini functions in this class
    # so that we can use it for .fastfs config

    @safe_write()
    def write_ini(self, file, data: dict):

        config = configparser.ConfigParser()
        config.read_dict(data)
        config.write(file)

    @safe_read()
    def read_ini(self, file):
        config = configparser.ConfigParser()
        config.read_file(file)
        return {s: dict(config.items(s)) for s in config.sections()}
