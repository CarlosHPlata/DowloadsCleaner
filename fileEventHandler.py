from fileCleaner import FileCleaner
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from time import sleep

class FileEventHandler( FileSystemEventHandler ):

    def __init__(self, src_path:Path, destination_path:Path):
        self.__src_path = src_path
        self.__destination_path = destination_path


    def on_modified(self, event):
        sleep(5)
        cleaner = FileCleaner(src_path = self.__src_path, destination_path = self.__destination_path)
        cleaner.clean()
        