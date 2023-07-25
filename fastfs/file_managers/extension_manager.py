from fastfs.file_managers.abstract_file_manager import AbstractFileManager
from fastfs.decorators import safe_read, safe_write, path_replace

from typing import Any, Union, List, Tuple

from fastfs.exceptions import InvalidFileDataError, CorruptFileError, FileNotFound, MissingDependencyError, FileWriteError, FileReadError

try:
    import yaml
except ImportError:
    yaml = None

try:
    import h5py
except ImportError:
    h5py = None

try:
    import pandas as pd
except ImportError:
    pd = None


class ExtensionFileManager(AbstractFileManager):

    @safe_write()
    def write_yaml(self, file, data: Any):
        try:
            if yaml is None:
                raise MissingDependencyError("PyYAML")

            yaml.dump(data, file)
        except yaml.YAMLError as exc:
            raise InvalidFileDataError('Failed to write YAML data.') from exc

    @safe_read()
    def read_yaml(self, file):
        try:
            if yaml is None:
                raise MissingDependencyError("PyYAML")

            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            raise CorruptFileError('Failed to read YAML data.') from exc

    @path_replace
    def write_hdf5(self, file_name: str, data: Any):
        try:
            if h5py is None:
                raise MissingDependencyError("hyp5")

            with h5py.File(file_name, 'w') as f:
                f.create_dataset('data', data=data)
        except (OSError, PermissionError, IsADirectoryError, InvalidFileDataError) as exc:
            raise FileWriteError from exc

    @path_replace
    def read_hdf5(self, file_name: str):
        try:
            if h5py is None:
                raise MissingDependencyError("hyp5")

            with h5py.File(file_name, 'r') as f:
                return f['data'][()]
        except FileNotFoundError as exc:
            raise FileNotFound(file_name) from exc
        except (OSError, PermissionError, IsADirectoryError) as exc:
            raise FileReadError from exc

    @path_replace
    def write_dataframe(self, file_name: str, data: Any):
        try:
            if pd is None:
                raise MissingDependencyError("pandas")

            with h5py.File(file_name, 'w') as f:
                f.create_dataset('data', data=data)
        except (OSError, PermissionError, IsADirectoryError, InvalidFileDataError) as exc:
            raise FileWriteError from exc

    @path_replace
    def read_dataframe(self, file_name: str):
        try:
            if pd is None:
                raise MissingDependencyError("pandas")

            file_extension = self.get_file_extension(file_name)

            

        except FileNotFoundError as exc:
            raise FileNotFound(file_name) from exc
        except (OSError, PermissionError, IsADirectoryError) as exc:
            raise FileReadError from exc