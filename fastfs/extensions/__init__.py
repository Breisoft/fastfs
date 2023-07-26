from typing import Any, Union, List, Callable

from fastfs.global_instance import fast_file_manager


def write_yaml(file_name: str, data: Any):
    """
    Writes data to a YAML file.

    Args:
        file_name: The name/path of the file to write the YAML data to.
        data: The data to write as a YAML object.
    """
    fast_file_manager.write_yaml(file_name, data)


def read_yaml(file_name: str) -> Any:
    """
    Reads data from a YAML file.

    Args:
        file_name: The name/path of the YAML file to read from.

    Returns:
        Any: The data read from the YAML file.
    """
    return fast_file_manager.read_yaml(file_name)


def write_hdf5(file_name: str, data: Any):
    """
    Writes data to an HDF5 file.

    Args:
        file_name: The name/path of the file to write the HDF5 data to.
        data: The data to write as an HDF5 object.
    """
    fast_file_manager.write_hdf5(file_name, data)


def read_hdf5(file_name: str) -> Any:
    """
    Reads data from an HDF5 file.

    Args:
        file_name: The name/path of the HDF5 file to read from.

    Returns:
        Any: The data read from the HDF5 file.
    """
    return fast_file_manager.read_hdf5(file_name)


def write_dataframe(file_name: str, dataframe: 'pd.DataFrame', sep: str = ',', header: Union[bool, List[str]] = True, index: bool = True):
    """
    Writes a pandas dataframe to a CSV file. If the extension provided in 'file_name' is not '.csv' it will be changed to that.

    Args:
        file_name: The name/path of the file to write the data to.
        dataframe: The data to write as a pandas DataFrame.
        sep (optional): The delimiter character for the csv output file.
        header (optional): Write out the column names. If a list of strings is given it is assumed to be aliases for the column names.
        index (optional): Write row names (index).
    """

    fast_file_manager.write_dataframe(
        file_name, dataframe, sep=sep, header=header, index=index)


def read_dataframe(file_name: str, sep: str = ','):
    """
    Reads a pandas dataframe from a CSV, JSON, or PICKLE file.

    Args:
        file_name: The name/path of the file to read the data from.
        sep (optional): The delimiter character if the input file is a CSV.
    """

    return fast_file_manager.read_dataframe(file_name, sep=sep)
