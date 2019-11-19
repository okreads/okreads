import os


class ExistingFile:

    def __init__(self, location: str):
        if not os.path.exists(location):
            raise Exception("File does not exist")

        self.location = location
