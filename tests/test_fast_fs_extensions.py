import os
import unittest
from typing import List
import shutil
from fastfs.extensions import write_dataframe, read_dataframe, write_hdf5, read_hdf5, write_yaml, read_yaml


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


class TestFastFsExtensions(unittest.TestCase):

    def setUp(self):
        # Setup a test directory in the current directory
        self.test_dir = os.path.join(os.getcwd(), 'test_dir')

        os.mkdir(self.test_dir)

        self.df_path = os.path.join(self.test_dir, 'pd_test.csv')
        self.h5_path = os.path.join(self.test_dir, 'test.hdf5')
        self.yaml_path = os.path.join(self.test_dir, 'test.yml')

    def tearDown(self):
        # Delete the test directory after running the tests
        shutil.rmtree(self.test_dir)

    def test_dataframe_file_write_and_read(self):

        if pd is None:
            self.skipTest(
                'pandas optional dependency is not installed. Skipping test...')

        test_data = {'col1': ['test', '456']}

        df = pd.DataFrame.from_dict(test_data)
        df.columns = df.columns.astype(str)

        write_dataframe(self.df_path, df, index=False)

        file_df = read_dataframe(self.df_path)
        file_df.columns = file_df.columns.astype(str)

        # Convert dataframes to dictionary and compare
        self.assertDictEqual(df.to_dict(), file_df.to_dict())

    def test_hdf5_file_write_and_read(self):

        if h5py is None:
            self.skipTest(
                'h5py optional dependency is not installed. Skipping test...')

        # Create a simple list as the test data
        data = [1, 2, 3, 4, 5]

        # Write the data to a HDF5 file
        write_hdf5(self.h5_path, data)

        # Read the data back from the HDF5 file
        file_data = read_hdf5(self.h5_path)

        # Compare the original data and the data read from file
        self.assertListEqual(data, list(file_data))

    def test_yaml_file_write_and_read(self):

        if yaml is None:
            self.skipTest(
                'PyYAML optional dependency is not installed. Skipping test...')

        # Create a dictionary as test data
        data = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

        # Write the data to a YAML file
        write_yaml(self.yaml_path, data)

        # Read the data back from the YAML file
        file_data = read_yaml(self.yaml_path)

        # Compare the original data and the data read from file
        self.assertDictEqual(data, file_data)


if __name__ == '__main__':
    unittest.main()
