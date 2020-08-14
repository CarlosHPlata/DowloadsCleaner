from fileCleaner import FileCleaner
from fileEventHandler import FileEventHandler

from watchdog.observers import Observer
import sys
from time import sleep
from pathlib import Path

SRC_PATH = Path.home() / 'Downloads'
DESTINATION_PATH = Path.home()


class BackgroundProcess:

    def run(self):
        event_handler = FileEventHandler(SRC_PATH, DESTINATION_PATH)
        observer = Observer()
        observer.schedule(event_handler, f'{SRC_PATH}', recursive=True)
        observer.start()

        try:
            while True:
                sleep(60)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()
        print('finished successfully')
        




if __name__ == '__main__':
    args = sys.argv
    
    if 'bg' in args:
        print('scanning for file changes')
        background = BackgroundProcess()
        background.run()

    else:
        cleaner = FileCleaner(src_path = SRC_PATH, destination_path = DESTINATION_PATH)
        cleaner.clean()
