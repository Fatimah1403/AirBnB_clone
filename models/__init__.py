#!/usr/bin/python3
"""
Initializes the package and storage system for
Reloads FileStorage contents
Loads any existing data from disk into memory using reload()
"""
from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
