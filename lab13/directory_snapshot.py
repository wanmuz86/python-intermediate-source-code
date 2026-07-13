# THis is the class to represent our directory
# We need this to use Pickle
# Pickle need to be saved as "Class object"

class DirectorySnapshot:

    def __init__(self, base_bath, files):
        self.base_bath = str(base_bath)
        self.files = files

    def summary(self):
        return f"{len(self.files)} files in {self.base_bath}"