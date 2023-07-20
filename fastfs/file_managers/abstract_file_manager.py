from fastfs.file_managers.base_file_manager import safe_read, safe_write, path_replace
from fastfs.file_managers.extension_manager import ExtensionFileManager
from fastfs.types import FileTypes

from typing import Any, List, Union, Callable

import json
import os
import time

class AbstractFileManager(ExtensionFileManager):

    @path_replace
    def get_file_extension(self, file_name):
        return os.path.splitext(file_name)[1]

    @path_replace
    def get_directory_info(self, directory_name):
        info = {}
    
        # Check if directory exists
        if os.path.isdir(directory_name):
            # Get the absolute path of the directory
            info["absolute_path"] = os.path.abspath(directory_name)
            
            # Get the number of files in the directory
            info["num_files"] = len(os.listdir(directory_name))
            
            # Get the creation time of the directory
            creation_time = os.path.getctime(directory_name)
            info["creation_time"] = time.ctime(creation_time)
            
            # Get the modification time of the directory
            modification_time = os.path.getmtime(directory_name)
            info["modification_time"] = time.ctime(modification_time)
            
            # Get the size of the directory
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(directory_name):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)
            info["total_size"] = total_size

        else:
            raise ValueError(f"{directory_name} does not exist")
        
        return info
    
    @path_replace
    def get_file_info(self, file_name):
        info = {}
        
        # Check if file exists
        if os.path.isfile(file_name):
            # Get the absolute path of the file
            info["absolute_path"] = os.path.abspath(file_name)
            
            # Get the creation time of the file
            creation_time = os.path.getctime(file_name)
            info["creation_time"] = time.ctime(creation_time)
            
            # Get the modification time of the file
            modification_time = os.path.getmtime(file_name)
            info["modification_time"] = time.ctime(modification_time)
            
            # Get the size of the file
            info["size"] = os.path.getsize(file_name)
            
            # Get file extension
            info["extension"] = self.get_file_extension(file_name)
        
        else:
            raise ValueError(f"{file_name} does not exist")
        
        return info


    @safe_write()
    def write_lines(self, file, lines: list):

        for line in lines:
            file.write(line + os.linesep)

    @safe_read()
    def read_lines(self, file):
        lines = [line.strip() for line in file.readlines()]

        return lines

    @safe_read(context_manager=False)
    def iter_lines(self, file):
        for line in file:
            yield line

        file.close()        

    def bulk_write_directory(self, directory_name: str, file_data_ls: List[Any], data_type: Union[FileTypes, str],
                              file_prefix: Union[None, str]=None):
        
        if data_type not in FileTypes._value2member_map_:
            raise ValueError('Unsupported data_type, supported types: %s', FileTypes._member_names_)

        if isinstance(data_type, str):
            data_type = FileTypes[data_type.upper()]

        # First, create the directory if it doesn't exist
        self.touch_directory(directory_name)

        file_extension = data_type.value
        
        # Then, iterate over the file data and write each file
        for idx, file_data in enumerate(file_data_ls):

            full_path = f'{directory_name}/{idx}'

            if file_prefix is not None:
                full_path += f'-{file_prefix}'

            full_path += f'.{file_extension}'

            if data_type == FileTypes.JSON:
                self.write_json(full_path, file_data)
            elif data_type == FileTypes.PICKLE:
                self.write_pickle(full_path, file_data)
            elif data_type == FileTypes.CSV:
                self.write_csv(full_path, file_data)
            elif data_type == FileTypes.BINARY:
                self.write_binary(full_path, file_data)

    def bulk_read_directory(self, directory_name: str, skip_unsupported_data_type: bool=False, 
                            sort_by: Callable=None, sort_reverse=False, 
                            file_prefix: Union[None, str]=None, include_file_names: bool=False) -> List[Any]:
        data = {}

        if sort_by == None:

            if file_prefix == None:
                sort_by = lambda file_name: int(file_name.replace(self.get_file_extension(file_name), ''))
            else:
                sort_by = lambda file_name: int(file_name.split("-")[0])


        for file_name in self.sorted_ls(directory_name, sort_by=sort_by, reverse=sort_reverse):

            file_extension = self.get_file_extension(file_name).replace('.', '')

            if file_extension == 'json':
                data[file_name] = self.read_json(f"{directory_name}/{file_name}")
            elif file_extension == 'pickle':
                data[file_name] = self.read_pickle(f"{directory_name}/{file_name}")
            # ...add other data types as needed...
            else:

                if skip_unsupported_data_type:
                    continue

                raise ValueError('Unsupported file extension: %s', file_extension)
        
        if include_file_names:
            return data
        else:
            return list(data.values())