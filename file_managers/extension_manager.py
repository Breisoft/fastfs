from fastfs.file_managers.base_file_manager import BaseFileManager
from fastfs.decorators import safe_read, safe_write, path_replace

import json
import pickle
import csv

from typing import Any, Callable, Union, List

from fastfs.exceptions import InvalidFileDataError, CorruptFileError, FileNotFound, MissingDependencyError, FileWriteError, FileReadError

try:
    import yaml
except ImportError:
    yaml = None

try:
    import h5py
except ImportError:
    h5py = None


class DefaultExtensionManager(BaseFileManager):

    @safe_write(write_mode='wb')
    def write_binary(self, file, file_data: bytes):
        if not isinstance(file_data, bytes):
            raise ValueError("Data should be bytes for writing binary.")
        file.write(file_data)

    @safe_read(read_mode='rb')
    def read_binary(self, file):
        return file.read()

    @safe_write(write_mode='wb')
    def write_pickle(self, file, file_data):

        try:
            pickle.dump(file_data, file)
        except pickle.PicklingError as exc:
            raise InvalidFileDataError(
                'Object may not be serializable.') from exc
        except (OverflowError, MemoryError, AttributeError) as exc:
            raise FileWriteError from exc

    @safe_read(read_mode='rb')
    def read_pickle(self, file):

        try:
            return pickle.load(file)
        except pickle.UnpicklingError as exc:
            raise CorruptFileError('Failed to unpickle the file.') from exc
        except EOFError as exc:
            raise CorruptFileError(
                'Unexpected end of file while reading pickle data.') from exc
        except AttributeError as exc:
            raise CorruptFileError(
                'A required attribute was not found.') from exc
        except ImportError as exc:
            raise MissingDependencyError(
                '(see above exception)') from exc
        except pickle.PickleError as exc:
            raise CorruptFileError(
                'An error occured while unpickling.') from exc

    @safe_write()
    def write_json(self, file, file_data):

        try:
            json.dump(file_data, file)
        except TypeError as exc:
            raise InvalidFileDataError(
                'Failed to serialize the data.') from exc
        except OverflowError as exc:
            raise InvalidFileDataError(
                'The data is too deeply nested.') from exc
        except json.JSONDecodeError as exc:
            raise InvalidFileDataError('Could not encode JSON.') from exc

    @safe_read()
    def read_json(self, file):
        try:
            return json.load(file)
        except json.JSONDecodeError as exc:
            raise InvalidFileDataError('Could not decode JSON.') from exc

    @safe_write()
    def write_csv(self, file, file_data: Union[List[dict], List[list]], header: Union[None, list] = None):

        first_item = file_data[0]

        try:

            if isinstance(first_item, dict):
                field_names = first_item.keys()
                writer = csv.DictWriter(file, fieldnames=field_names)
                writer.writeheader()
            else:
                if header is None:
                    raise InvalidFileDataError(
                        "A header is required when using a list of lists for CSV file data.")

                writer = csv.writer(file)
                writer.writerow(header)

            # Write the actual data
            writer.writerows(file_data)
        except csv.Error as exc:
            raise InvalidFileDataError('Failed to write CSV data.') from exc
        except (AttributeError, TypeError) as exc:
            raise InvalidFileDataError('The data is not writable.') from exc


class ExtensionFileManager(DefaultExtensionManager):

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
