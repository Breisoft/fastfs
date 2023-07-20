from fastfs.file_managers.append_file_manager import AppendFileManager
from fastfs.file_managers.abstract_file_manager import AbstractFileManager

class FastFileManager(AppendFileManager, AbstractFileManager):
    pass
   

# creating a global FileManager instance
fast_file_manager = FastFileManager()
