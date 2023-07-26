# fastfs

fastfs is a comprehensive and efficient Python library designed to bridge the gap in Python's file management capabilities. It encapsulates powerful features for reading, writing, and managing data across a variety of file formats and for handling complex directory structures.

## Features

- **Versatile Data Handling**: FastFS offers extensive functions for reading and writing data across a multitude of formats, including JSON, CSV, Pickle, HDF5, INI, and YAML.

- **Advanced Directory Management**: FastFS revolutionizes the way directory structures are handled in Python. By operating relative to a specified 'fastfs' directory, it ensures efficient and user-friendly management of your file system.

## Installation

You can install FastFS using pip:

```bash
pip install fastfs
```

fastfs has a few optional dependencies for enhanced functionality:

pandas>=0.20.0 (Required for DataFrame-related functionality)
h5py>=2.5.0 (Required for HDF5-related functionality)
PyYAML>=3.11 (Required for YAML-related functionality)
These libraries are not mandatory for the installation and basic functionality of FastFS, but some features will not be available without them. You can install them separately if needed.

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

# #Documentation

You can find more detailed documentation and usage examples in the docs directory.

## Contributing

We welcome contributions! Please see our CONTRIBUTING.md file for details.

## License

FastFS is licensed under the MIT license. Please see the LICENSE file for details.
