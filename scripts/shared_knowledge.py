import os
from typing import List

class SharedKnowledge:
    """
    A class to represent a shared knowledge base.

    Attributes
    ----------
    storage_dir : str
        Directory where knowledge files are stored.

    Methods
    -------
    upload_file(file_path: str) -> str:
        Uploads a file to the shared knowledge storage.
    list_files() -> List[str]:
        Lists all files in the shared knowledge storage.
    retrieve_file(file_name: str) -> str:
        Retrieves the path of a file in the shared knowledge storage.
    """

    # Why: Initializes the storage directory to ensure all file operations have a valid target.
    def __init__(self, storage_dir: str = "docs/knowledge"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    # Why: Validates file existence before attempting to upload, preventing runtime errors.
    def upload_file(self, file_path: str) -> str:
        """
        Uploads a file to the shared knowledge storage.

        Args:
            file_path (str): Path to the file to upload.

        Returns:
            str: The path where the file is stored.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        file_name = os.path.basename(file_path)
        destination = os.path.join(self.storage_dir, file_name)
        with open(file_path, 'rb') as src, open(destination, 'wb') as dest:
            dest.write(src.read())

        return destination

    # Why: Provides a list of all stored files for easy retrieval and management.
    def list_files(self) -> List[str]:
        """
        Lists all files in the shared knowledge storage.

        Returns:
            List[str]: List of file names in the storage.
        """
        return os.listdir(self.storage_dir)

    # Why: Ensures that only existing files are retrieved, maintaining data integrity.
    def retrieve_file(self, file_name: str) -> str:
        """
        Retrieves the path of a file in the shared knowledge storage.

        Args:
            file_name (str): Name of the file to retrieve.

        Returns:
            str: The full path to the file.
        """
        file_path = os.path.join(self.storage_dir, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_name}")

        return file_path

# Example usage
if __name__ == "__main__":
    knowledge = SharedKnowledge("./shared_knowledge_storage")
    print("Storage initialized.")

    # Example: Upload a file
    try:
        uploaded_path = knowledge.upload_file("example.txt")
        print(f"File uploaded to: {uploaded_path}")
    except FileNotFoundError as e:
        print(e)

    # Example: List files
    print("Files in storage:", knowledge.list_files())

    # Example: Retrieve a file
    try:
        file_path = knowledge.retrieve_file("example.txt")
        print(f"File retrieved at: {file_path}")
    except FileNotFoundError as e:
        print(e)