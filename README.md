# fastfs

fastfs is a comprehensive and efficient Python library designed to bridge the gap in Python's file management capabilities. It encapsulates powerful features for reading, writing, and managing data across a variety of file formats and for handling complex directory structures.

## Features

- **Versatile Data Handling**: fastfs offers extensive functions for reading and writing data across a multitude of formats, including JSON, CSV, Pickle, HDF5, INI, and YAML.

- **Advanced Directory Management**: fastfs revolutionizes the way directory structures are handled in Python. By operating relative to a specified 'fastfs' directory, it ensures efficient and user-friendly management of your file system.

## Installation

You can install fastfs using pip:

```bash
pip install fastfs
```

fastfs has a few optional dependencies for enhanced functionality:

- pandas>=0.20.0 (Required for DataFrame-related functionality)
- h5py>=2.5.0 (Required for HDF5-related functionality)
- PyYAML>=3.11 (Required for YAML-related functionality)

These libraries are not mandatory for the installation and basic functionality of fastfs, but some features will not be available without them. You can install them separately if needed.

To install fastfs along with all optional dependencies, use the following command:

```bash
pip install fastfs[full]
```

## Getting Started

Here's a basic example of how to use fastfs:

```python
from fastfs import read_json, write_json

# Write a test JSON file
json_data = {'hello': 'world'}

write_json('test_file.json', json_data)

# Read a JSON file
json_data = read_json('test_file.json')

print(json_data)
```

Here's how to use fastfs's relative directory system

```python
from fastfs.utils import create_fs

# For this example, let's say your current working directory is Documents.

# Create a folder called 'files' in the working directory
# By default, we want to set active=True, that means that all paths
# will be set to relative paths, active=False will disable the system.
create_fs('files', active=True)

# In the previous example, this would create 'test_file.json' in Documents
# but now that we have a fastfs directory enabled, it will automatically go to Documents/files/test_file.json
# when fastfs is active, all paths with fastfs functions will be relative to the fastfs folder
write_json('test_file.json', json_data)

# This persists between processes as well, as the data is stored in a hidden file called .fastfs
# this stores whether it's active or not, and what the directory name is.
```

one of the most useful features of fastfs is the ability to quickly map a series of files to a directory

```python
from fastfs.utils import bulk_write_directory, bulk_read_directory
from fastfs.data_types import FileTypes


# Let's say we have a list of data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Let's say we want to map out this entire list to a directory named 'ten-files.'
# This function will automatically create a 10 files in the 'ten-files' directory:
# 1.pkl, 2.pkl, 3.pkl, etc. with the corresponding data from the data list saved inside.
bulk_write_directory('ten-files', data, 'pickle')

# FileTypes enum is also supported for cleaner code!
bulk_write_directory('ten-files', data, FileTypes.PICKLE)

# To load, all we do is the same thing with bulk_read_directory
# bulk_read_directory automatically detects the data type
data = bulk_read_directory('ten-files')

# Have a pre-existing file directory with a more complicated naming scheme than '1.xyz, 2.xyz, 3.xyz?'
# you can pass in any lambda you want to sort the files!
data = bulk_read_directory('ten-files',
                    sort_by=lambda x: int(x.replace('myfile-', '').strip()),
                    )

# bulk_read_directory also supports:
# skipping fastfs unsupported data types
# sort_by_reverse
# file_prefix ('myfile-' in the above example)
# include_file_names (returns a dictionary where the key is the file name and the value is the file's contents)
```

fastfs even supports dataframes if pandas is installed!

```python
from fastfs.extensions import write_dataframe, read_dataframe
import pandas as pd

# Create a dictionary of data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save the dataframe to a file with optional args
write_dataframe('df.csv', df, sep=',', header=True)

# Read the dataframe to a file with optional args
df = read_dataframe('df.csv', sep=',')
```

fastfs also has file/directory utility functions:

```py

from fastfs.utils import ls, sorted_ls, file_exists, touch_file, delete_file, touch_directory, delete_directory
from fastfs.utils import get_directory_info, get_file_info

# Returns a list of all file names in the 'files' directory
ls('files')

# Same functionality as ls, but requires a callable sort function
sorted_ls('files', lambda x: int(x.replace('myfile-', '').strip(), reverse=False)

# Returns True if file exists, False if not
file_exists('test.txt')

# Creates a file if it doesn't already exist
touch_file('test.txt')

# Deletes a file
# NOTE: DOES NOT ASK FOR CONFIRMATION, USE AT YOUR OWN RISK
delete_file('test.txt')

# Creates a directory if it doesn't already exist
touch_directory('files')

# Deletes a directory and all sub-directories/files within
# NOTE: DOES NOT ASK FOR CONFIRMATION, USE AT YOUR OWN RISK
delete_directory('files')

# Returns a dictionary returning metadata on a file including the absolute path, creation time,
# modification time, size, and extension
get_file_info('test.txt')

# Returns a dictionary returning metadata on a directory including the absolute path, number of files,
# creation time, modification time, and total size.
get_directory_info('files')

```

## Supported file types

Currently, fastfs supports the following file types:

- PICKLE: ('pickle', 'pkl')
- JSON: 'json'
- BINARY: ('bin', 'binary', 'dat')
- CSV: 'csv'
- HDF5: 'hdf5'
- INI: 'ini'
- YAML: ('yaml', 'yml')

## Documentation

You can find more detailed documentation in the docs directory.

## Contributing

We welcome contributions! Please see our CONTRIBUTING.md file for details.

## License

fastfs is licensed under the MIT license. Please see the LICENSE file for details.
