import uuid



class File():

    def __init__(self, file_url, content_type, content_length, last_modified):
        self.id = str(uuid.uuid4())
        self.file_url = file_url
        self.content_type = content_type
        self.content_length = content_length
        self.last_modified = last_modified
        

    def __str__(self):
        return "{0} ,{1}, {2}, {3}, {4}".format(self.id, self.file_url, self.content_type, self.content_length, self.last_modified)