class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

obj = FileStorage()
obj.id = 45
print(obj.all)