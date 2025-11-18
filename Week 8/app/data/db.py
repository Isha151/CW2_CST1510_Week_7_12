import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]  # project root
DB_PATH = BASE_DIR / "DATA" / "intelligence_platform.db"

def connect_database(db_path=DB_PATH):
    # Create DATA directory if missing
    db_path.parent.mkdir(parents=True, exist_ok=True)

    # Create database
    return sqlite3.connect(str(db_path))

if __name__ == "__main__":
    connect_database()
    print("Database created at:", DB_PATH)
