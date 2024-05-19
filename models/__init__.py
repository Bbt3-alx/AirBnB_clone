#!/usr/bin//python3
"""The moduleinit to instantiate the storage"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
