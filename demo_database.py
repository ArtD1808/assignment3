"""Create and verify a small SQLite database for Assignment 3."""

import sqlite3
from pathlib import Path

DATABASE = Path(__file__).resolve().parent / "demo.sqlite3"


def main() -> None:
    if DATABASE.exists():
        raise FileExistsError(f"Refusing to overwrite {DATABASE}")
    with sqlite3.connect(DATABASE) as connection:
        connection.execute(
            "CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT NOT NULL)"
        )
        connection.execute(
            "INSERT INTO items (id, name) VALUES (?, ?)", (1, "Sample")
        )
    with sqlite3.connect(DATABASE) as connection:
        row = connection.execute(
            "SELECT id, name FROM items WHERE id = ?", (1,)
        ).fetchone()
        if row != (1, "Sample"):
            raise RuntimeError(f"Unexpected record: {row!r}")
        integrity = connection.execute("PRAGMA integrity_check").fetchone()
        if integrity != ("ok",):
            raise RuntimeError(f"Database integrity check failed: {integrity!r}")
        print(f"SQLite {sqlite3.sqlite_version}; reopened record: {row}")
        print("Database integrity: ok")


if __name__ == "__main__":
    main()
