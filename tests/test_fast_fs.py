import os
import unittest
from fastfs import write_pickle, read_pickle, write_json, read_json, write_lines, read_lines, write_csv, read_csv, write_file, read_file, write_ini, read_ini

import shutil

class FastFSTests(unittest.TestCase):

    def _get_path(self, file_name):

        return os.path.join(self.test_dir, file_name)

    def setUp(self):
        self.test_dir = "test_files"
        self.test_data = {"test": "FastFS Unit Test"}

         # Prepare the test directory
        if not os.path.exists(self.test_dir):
            os.mkdir(self.test_dir)

        self.pickle_path = self._get_path('test.pkl')
        self.json_path = self._get_path('test.json')
        self.csv_path = self._get_path('test.csv')
        self.file_path = self._get_path('test.txt')
        self.ini_path = self._get_path('test.ini')

    def tearDown(self):
    
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)


    # Tests for write_pickle & read_pickle methods
    def test_pickle_file_write_and_read(self):
        # Writing to pickle file
        write_pickle(self.pickle_path, self.test_data)

        # Verifying if file is created
        self.assertTrue(os.path.exists(self.pickle_path))

        # Reading from pickle file
        read_data = read_pickle(self.pickle_path)

        # Verification
        self.assertEqual(self.test_data, read_data)

    # Tests for write_json & read_json methods
    def test_json_file_write_and_read(self):
        # Writing to json file
        write_json(self.json_path, self.test_data)

        # Verifying if file is created
        self.assertTrue(os.path.exists(self.json_path))

        # Reading from json file
        read_data = read_json(self.json_path)

        # Verification
        self.assertEqual(self.test_data, read_data)

    # Tests for write_lines & read_lines methods
    def test_lines_write_and_read(self):
        lines = ['Line 1', 'Line 2', 'Line 3']

        # Writing to file
        write_lines(self.file_path, lines)

        # Reading from file
        read_lines_data = read_lines(self.file_path)

        # Verification
        self.assertEqual(lines, read_lines_data)

    def test_csv_write_and_read_with_headers(self):

        # Test data for writing and reading
        headers = ['Name', 'Age', 'Occupation']
        data_lists = [['Alice', '30', 'Engineer'],
                      ['Bob', '40', 'Doctor']]

        # Write and read as list of lists
        write_csv(self.csv_path, data_lists, header=headers)
        read_headers, read_data = read_csv(self.csv_path, return_list_of_dicts=False)
        self.assertEqual(headers, read_headers)
        self.assertEqual(data_lists, read_data)

    def test_csv_write_and_read_no_headers(self):

        # Test data for writing and reading
        data_dicts = [{'Name': 'Alice', 'Age': '30', 'Occupation': 'Engineer'},
                      {'Name': 'Bob', 'Age': '40', 'Occupation': 'Doctor'}]
   

        # Write and read as list of dicts
        write_csv(self.csv_path, data_dicts)
        read_data = read_csv(self.csv_path, return_list_of_dicts=True)
        self.assertEqual(data_dicts, read_data)

    def test_file_write_and_read(self):
        # Test data for writing and reading
        data = 'This is some test data.'

        # Write data to file
        write_file(self.file_path, data)

        # Read data back from file
        read_data = read_file(self.file_path)

        self.assertEqual(data, read_data)

    def test_ini_write_and_read(self):

        data = {'test': 'value'}

        write_ini(self.ini_path, data)

        read_data = read_ini(self.ini_path)

        self.assertEqual(data, read_data)


if __name__ == "__main__":

    unittest.main()
