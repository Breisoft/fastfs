from setuptools import setup, find_packages

setup(
    name='fastfs',
    version='0.0.0',
    url='http://github.com/breisoft/fastfs',
    author='Josh Breidinger',
    author_email='company@breisoft.com',
    description="""FastFS is a comprehensive and efficient Python library designed to bridge the gap in Python's file management capabilities. It encapsulates powerful features for reading, writing, and managing data across a variety of file formats and for handling complex directory structures.

FastFS supports a wide range of file formats, including JSON, CSV, Pickle, HDF5, INI, YAML, and XML. This makes it your one-stop solution for all data storage and retrieval needs, facilitating a seamless transition between different data formats within the Python environment.

One of FastFS's standout features is its robust directory management system. By handling all operations relative to a designated 'fastfs' directory, it simplifies file path handling, encouraging cleaner, more organized code.

Key features of FastFS include:

Versatile Data Handling: FastFS offers extensive functions for reading and writing data across a multitude of formats. Whether your data is in JSON, CSV, or any other supported format, FastFS has you covered.

Advanced Directory Management: FastFS revolutionizes the way directory structures are handled in Python. By operating relative to a specified 'fastfs' directory, it ensures efficient and user-friendly management of your file system.

The Missing Piece: Python's standard library, while powerful, lacks a dedicated, comprehensive system for file and directory management. FastFS fills this void, offering an intuitive, Pythonic interface to manage your files and directories.

FastFS is the missing piece in Python's file management ecosystem, designed to accelerate your data operations and enhance your productivity. Start using FastFS today and discover a faster, more efficient way to manage your file system in Python.""",
    packages=find_packages(),    
    install_requires=[],
)
