import os
import json
import pickle
import unittest
from unittest.mock import patch
from fastfs import write_pickle, read_pickle, write_json, read_json, write_lines, read_lines, create_fs, sorted_ls


class FastFSTests(unittest.TestCase):

    def setUp(self):
        self.file_name_pickle = "test.pkl"
        self.file_name_json = "test.json"
        self.data = {"test": "FastFS Unit Test"}

    def tearDown(self):
        if os.path.exists(self.file_name_pickle):
            os.remove(self.file_name_pickle)
        if os.path.exists(self.file_name_json):
            os.remove(self.file_name_json)

    # Tests for write_pickle & read_pickle methods
    def test_pickle_file_write_and_read(self):
        # Writing to pickle file
        write_pickle(self.file_name_pickle, self.data)

        # Verifying if file is created
        self.assertTrue(os.path.exists(self.file_name_pickle))

        # Reading from pickle file
        read_data = read_pickle(self.file_name_pickle)

        # Verification
        self.assertEqual(self.data, read_data)

    # Tests for write_json & read_json methods
    def test_json_file_write_and_read(self):
        # Writing to json file
        write_json(self.file_name_json, self.data)

        # Verifying if file is created
        self.assertTrue(os.path.exists(self.file_name_json))

        # Reading from json file
        read_data = read_json(self.file_name_json)

        # Verification
        self.assertEqual(self.data, read_data)

    # Tests for write_lines & read_lines methods
    def test_file_lines_write_and_read(self):
        lines = ['Line 1', 'Line 2', 'Line 3']

        # Writing to file
        write_lines(self.file_name_pickle, lines)

        # Reading from file
        read_lines_data = read_lines(self.file_name_pickle)

        # Verification
        self.assertEqual(lines, read_lines_data)

    # Test for create_fastfs method
    @patch('fastfs.fast_file_manager.create_fs')
    def test_create_fs(self, mock_create_fs):
        create_fs('test_files')
        # Verifying the call
        mock_create_fs.assert_called_once_with('test_files', True)

    # Test for sorted_ls method
    @patch('fastfs.fast_file_manager.sorted_ls')
    def test_sorted_ls(self, sorted_ls):
        sorted_ls('test_files')
        # Verifying the call
        sorted_ls.assert_called_once_with('test_files', None, False)


if __name__ == "__main__":
    unittest.main()
