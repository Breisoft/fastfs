from fastfs.file_managers.base_file_manager import BaseFileManager, safe_read, safe_write, path_replace

from typing import Any

import json
import pickle
import csv

from typing import Any, Callable, Union, List

try:
    import yaml
except ImportError:
    yaml = None

try:
    import h5py
except ImportError:
    h5py = None

try:
    import pyarrow.parquet as pq
except ImportError:
    pq = None


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
        pickle.dump(file_data, file)

    @safe_read(read_mode='rb')
    def read_pickle(self, file):
        return pickle.load(file)

    @safe_write()
    def write_json(self, file, file_data):
        json.dump(file_data, file)


    @safe_write()
    def write_csv(self, file, file_data: Union[List[dict], List[list]], header: Union[None, list]=None):

        first_item = file_data[0]

        if isinstance(first_item, dict):
            field_names = first_item.keys()
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
        else:
            if header is None:
                raise Exception('Header should not be none if using a list of lists!')

            writer = csv.writer(file)
            writer.writerow(header)

        # Write the actual data
        writer.writerows(file_data)

    @safe_read()
    def read_json(self, file):
        return json.load(file)


class ExtensionFileManager(DefaultExtensionManager):

    @safe_write()
    def write_yaml(self, file, data: Any):

        if yaml == None:
            raise ImportError("The PyYAML package is required to use the write_yaml function. Install with `pip install fastfs[yaml]`.")

        yaml.dump(data, file)

    @safe_read()
    def read_yaml(self, file):
        
        if yaml == None:
            raise ImportError("The PyYAML package is required to use the read_yaml function. Install with `pip install fastfs[yaml]`.")

        return yaml.safe_load(file)
    
    @path_replace
    def write_hdf5(self, file_name: str, data: Any):

        if h5py == None:
            raise ImportError("The hyp5 package is required to use the write_hdf5 function. Install with `pip install fastfs[hdf5]`.")

        with h5py.File(file_name, 'w') as f:
            f.create_dataset('data', data=data)

    @path_replace
    def read_hdf5(self, file_name: str):

        if h5py == None:
            raise ImportError("The hyp5 package is required to use the read_hdf5 function. Install with `pip install fastfs[hdf5]`.")

        with h5py.File(file_name, 'r') as f:
            return f['data'][()]