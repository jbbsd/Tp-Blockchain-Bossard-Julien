import uuid
import hashlib

class Block(object):
    def __init__(self):
        self.unique_id = uuid.uuid4()
