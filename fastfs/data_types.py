from enum import Enum


class FileTypes(Enum):
    PICKLE = ('pickle', 'pkl')
    JSON = 'json'
    BINARY = ('bin', 'binary', 'dat')
    CSV = 'csv'
    HDF5 = 'hdf5'
    INI = 'ini'
    YAML = ('yaml', 'yml')
