class FastFsException(Exception):
    """Base exception class for fastfs library."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class UnsupportedFileType(FastFsException):
    """Raised when an unsupported file type is used."""

    def __init__(self, file_type: str, supported_types: str = ''):

        if len(supported_types) > 0:
            self.message = f"The file type {file_type} is not supported. Supported types: {supported_types}"
        else:
            self.message = f"The file type {file_type} is not supported."

        super().__init__(self.message)


class MissingDependencyError(FastFsException):
    """Raised when a required dependency is not installed."""

    def __init__(self, dependency_name: str):
        self.message = f"The {dependency_name} package is not installed. Please install this package to use the requested feature."
        super().__init__(self.message)


class InvalidFileDataError(FastFsException):
    """Raised when the provided data does not match the expected format for the file type."""

    def __init__(self, explanation: str):
        self.message = f"The provided data does not match the expected format for the file type. {explanation}"
        super().__init__(self.message)


class CorruptFileError(FastFsException):
    def __init__(self, explanation: str):
        self.message = f"The file could not be read/written. {explanation}"
        super().__init__(self.message)


class FileNotFound(FastFsException):
    """Raised when a specified file is not found."""

    def __init__(self, file_name: str):
        self.message = f"The file {file_name} does not exist."
        super().__init__(self.message)


class DirectoryNotFound(FastFsException):
    """Raised when a specified file is not found."""

    def __init__(self, file_name: str):
        self.message = f"The file {file_name} does not exist."
        super().__init__(self.message)


class FileWriteError(FastFsException):
    """Raised when there is an error writing to a file."""

    def __init__(self):
        self.message = "There was an error writing to the file."
        super().__init__(self.message)


class FileReadError(FastFsException):
    """Raised when there is an error reading from a file."""

    def __init__(self):
        self.message = "There was an error reading from the file."
        super().__init__(self.message)


class BulkReadDirectoryError(FastFsException):
    """Raised when there is an error from the bulk_read_directory function in AbstractFileManager."""

    def __init__(self, explanation: str):
        self.message = f"There was an error during bulk directory read. {explanation}"
        super().__init__(self.message)
