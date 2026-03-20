import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from processor import clean_and_load

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.xlsx'):
            time.sleep(1)  # Buffer for file copy completion
            try:
                rows = clean_and_load(event.src_path)
                print(f"Success: Ingested {rows} rows from {event.src_path}")
                shutil.move(event.src_path, "data/processed/")
            except Exception as e:
                print(f"Error processing {event.src_path}: {e}")
                shutil.move(event.src_path, "data/failed/")

# Initialize observer to watch the 'data/input/' directory