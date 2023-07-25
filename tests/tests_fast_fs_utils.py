import os
import unittest
from typing import List
import shutil
from fastfs.utils import sorted_ls, ls, file_exists, touch_file, touch_directory, delete_file, delete_directory, create_fs

class TestFastFsUtils(unittest.TestCase):

    def setUp(self):
        # Setup a test directory in the current directory
        self.test_dir = os.path.join(os.getcwd(), 'test_dir')

        os.mkdir(self.test_dir)

        self.test_file = 'test_file.txt'

    def tearDown(self):
        # Delete the test directory after running the tests
        shutil.rmtree(self.test_dir)

    def test_touch_directory(self):
        new_dir = os.path.join(self.test_dir, 'child_test_dir')

        touch_directory(new_dir)

        self.assertTrue(os.path.exists(new_dir))

    def test_delete_directory(self):
        new_dir = os.path.join(self.test_dir, 'child_test_dir')
        touch_directory(new_dir)

        self.assertTrue(os.path.exists(new_dir))

        delete_directory(new_dir)

        self.assertFalse(os.path.exists(new_dir))


    def test_file_exists(self):
        touch_file(self.test_file)
        self.assertTrue(file_exists(self.test_file))

    def test_ls(self):
        touch_file(os.path.join(self.test_dir, 'test_file.txt'))
        files: List[str] = ls(self.test_dir)
        self.assertIn('test_file.txt', files)  # Check if the created file is in the directory
    
    def test_sorted_ls(self):
        test_files = ['3.pkl', '1.pkl', '2.pkl']

        for file_name in test_files:
            with open(f"{self.test_dir}/{file_name}", "w") as f:
                f.write('')

        # Call the function
        sorted_files = sorted_ls(
            self.test_dir,
            lambda file_name: int(file_name.replace('.pkl', '')),
            reverse=False
        )

        # Assert that the files are sorted as expected
        self.assertEqual(sorted_files, ['1.pkl', '2.pkl', '3.pkl'])

        # Call the function with reverse
        reverse_sorted_files = sorted_ls(
            self.test_dir,
            lambda file_name: int(file_name.replace('.pkl', '')),
            reverse=True
        )

        # Assert that the files are reverse sorted as expected
        self.assertEqual(reverse_sorted_files, ['3.pkl', '2.pkl', '1.pkl'])

    def test_delete_file(self):
        touch_file(self.test_file)
        delete_file(self.test_file)
        self.assertFalse(file_exists(self.test_file))  # Check if file was deleted

if __name__ == '__main__':
    unittest.main()