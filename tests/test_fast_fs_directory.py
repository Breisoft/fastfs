import os
import json
import pickle
import unittest
from unittest.mock import patch, ANY
from fastfs import write_pickle
from fastfs.utils import create_fs, get_fs_directory, touch_directory

from fastfs.global_instance import fast_file_manager

import configparser

import shutil


class FastFSDirectoryTests(unittest.TestCase):
    """Tests the functionality of the .fastfs relative file system"""

    def setUp(self):
        self.fast_fs_dir = "test_fastfs_files"
        # Check that environment is clean before starting
        self.assertFalse(os.path.exists(self.fast_fs_dir))
        self.assertFalse(os.path.exists('.fastfs'))
        self.assertIsNone(fast_file_manager._local_fs)
        self.assertFalse(fast_file_manager._fs_active)

        # Create fs directory
        create_fs(self.fast_fs_dir, active=True)

    def _reset_fs_directory(self):
        if os.path.exists(self.fast_fs_dir):
            shutil.rmtree(self.fast_fs_dir)

        if os.path.exists('.fastfs'):
            os.remove('.fastfs')

        fast_file_manager._local_fs = None
        fast_file_manager._fs_active = False

    def tearDown(self):
        self._reset_fs_directory()

    def _test_create_fs(self, test_active):

        # Since it's created by default in setUp()
        self._reset_fs_directory()

        create_fs(self.fast_fs_dir, test_active)

        # Make sure files got created properly
        self.assertTrue(os.path.exists(self.fast_fs_dir),
                        f'{self.fast_fs_dir} does not exist')
        self.assertTrue(os.path.exists('.fastfs'), '.fastfs does not exist')

        # Create a ConfigParser object
        config = configparser.ConfigParser()

        # Read from a configuration file
        config.read('.fastfs')

        # Test that all of the values are in the config
        self.assertIn('DEFAULT', config,
                      'DEFAULT section missing from .fastfs')
        self.assertIn('directory', config['DEFAULT'],
                      'directory missing from DEFAULT section')
        self.assertIn('active', config['DEFAULT'],
                      'active missing from DEFAULT section')

        # Test that directory and active are proper values
        self.assertEqual(config['DEFAULT']['directory'], self.fast_fs_dir)

        active = config.getboolean('DEFAULT', 'active')

        self.assertEqual(active, test_active,
                         '.fastfs active is not the correct value!')

    def test_create_fs_active(self):

        self._test_create_fs(True)

    def test_create_fs_inactive(self):

        self._test_create_fs(False)

    def test_fs_relative_file_path(self):

        write_pickle('test.pkl', [])

        path = os.path.join(self.fast_fs_dir, 'test.pkl')

        self.assertTrue(path)

    def test_get_fs_directory(self):

        fs_directory = get_fs_directory()

        self.assertEqual(fs_directory, self.fast_fs_dir)

    def test_fs_relative_directory_path(self):
        test_directory = 'test_dir'

        touch_directory(test_directory)

        fs_path = os.path.join(self.fast_fs_dir, test_directory)

        # Make sure that the fastfs directory is being used
        self.assertTrue(os.path.exists(fs_path))
        self.assertFalse(os.path.exists(test_directory))

    def test_absolute_path(self):

        test_directory = 'test_dir'

        self.assertNotEqual(self.fast_fs_dir, test_directory)

        cwd = os.getcwd()

        full_path = os.path.join(cwd, test_directory)

        touch_directory(full_path)

        self.assertTrue(os.path.exists(full_path))

        # Make sure fastfs directory wasn't in use despite it being enabled because we're using an abs path
        self.assertFalse(os.path.exists(
            os.path.join(self.fast_fs_dir, test_directory)))

        # Delete the test directory
        shutil.rmtree(full_path)


if __name__ == "__main__":
    unittest.main()
