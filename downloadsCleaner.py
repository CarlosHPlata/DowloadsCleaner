from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from pathlib import Path
from time import sleep
import json
import shutil

class FileEventHandler(FileSystemEventHandler):
    
    def __init__(self, watch_path: Path):
        self.src_path = watch_path.resolve()

    
    def on_modified(self, event):
        for child in self.src_path.iterdir():
            if child.is_file():
                print(child.name)



if __name__ == '__main__':

    with open('filetypes.json') as file:
        files = json.load(file)
        formats = files['formats']
    
    if '.txt' in formats:
        print('its working bitch')

    watch_path = Path.home() / 'Desktop'
    event_handler = FileEventHandler(watch_path)
    
    observer = Observer()
    observer.schedule(event_handler, f'{watch_path}', recursive=True)
    observer.start()

    try :
        while True:
            print('looking for changes')
            sleep(20)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
    print('finished successfully')