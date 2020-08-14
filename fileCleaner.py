import json
import shutil
from pathlib import Path

class FileCleaner:

    __JSON_FILE_NAME = 'filetypes.json'

    def __init__(self, src_path:Path, destination_path:Path):
        self.__src_path = src_path.resolve()
        self.__destination_path = destination_path.resolve()
        self.__initJson()


    def __initJson(self):
        with open(self.__JSON_FILE_NAME) as json_file:
                json_obj = json.load(json_file)
                self.__file_types = json_obj['file_formats']
                self.__file_categories = json_obj['categories']



    def clean(self):
        for child in self.__src_path.iterdir():

            if child.is_file() and child.suffix.lower() in self.__file_types:
                destination = self.__get_destination_path(child)
                filename = self.__getNewFileName(child, destination)
                self.__moveFileToDestination(child, filename)


    def __get_destination_path(self, file):
        category = self.__file_types[ file.suffix.lower() ]
        category_destination = self.__destination_path / self.__file_categories[ category ]
        return category_destination


    def __getNewFileName(self, source, destination, increment = 0):
        if Path(destination / source):
            new_name = destination / f'{source.stem}_{increment}{source.suffix}'

            if not new_name.exists():
                return new_name
            else:
                return self.__getNewFileName(source, destination, increment = increment+1)
        
        else:
            return destination / source.name

    
    def __moveFileToDestination(self, file, destination):
        shutil.move( src=file, dst=destination )
        print('{0} moved to {1}'.format( file.name, f'{destination}' ))

