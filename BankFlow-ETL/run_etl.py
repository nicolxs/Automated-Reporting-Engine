"""Run the BankFlow ETL pipeline."""

import os
import sys

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from database import init_db

def main():
    """Initialize the database and start the file watcher."""
    print("Initializing BankFlow ETL Pipeline...")
    init_db()
    
    print("\nStarting file watcher...")
    from watcher import start_watcher
    start_watcher()

if __name__ == "__main__":
    main()
