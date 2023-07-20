from fastfs.file_managers.extension_manager import ExtensionFileManager
from typing import Any

import json

class AppendFileManager(ExtensionFileManager):

    def append_json(self, file_name: str, new_data: Any):
        
        existing_data = self.read_json(file_name)
    
        if not isinstance(existing_data, list):
            raise ValueError("Can only append to a JSON file if it contains a list.")

        existing_data.append(new_data)
        
        self.write_json(file_name, existing_data)
