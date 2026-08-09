import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from processor import clean_and_load

INPUT_DIR = "data/input"
PROCESSED_DIR = "data/processed"
FAILED_DIR = "data/failed"

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(('.xlsx', '.csv')):
            time.sleep(1)  # Buffer for file copy completion
            try:
                rows = clean_and_load(event.src_path)
                print(f"Success: Ingested {rows} rows from {event.src_path}")
                shutil.move(event.src_path, os.path.join(PROCESSED_DIR, os.path.basename(event.src_path)))
            except Exception as e:
                print(f"Error processing {event.src_path}: {e}")
                shutil.move(event.src_path, os.path.join(FAILED_DIR, os.path.basename(event.src_path)))

def start_watcher():
    """Start the file watcher to monitor the input directory."""
    # Ensure directories exist
    for dir_path in [INPUT_DIR, PROCESSED_DIR, FAILED_DIR]:
        os.makedirs(dir_path, exist_ok=True)
    
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=INPUT_DIR, recursive=False)
    observer.start()
    print(f"Watching for new files in {INPUT_DIR}...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Watcher stopped.")
    observer.join()

if __name__ == "__main__":
    start_watcher()