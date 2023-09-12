import os
import sqlite3

import click


@click.command()
@click.option("--sql-folder", required=True, help="Folder containing .sql files")
@click.option("--db-name", default="db.sqlite", help="Name of the SQLite database")
def import_sql_files(sql_folder, db_name):
    # Create or connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Loop through each .sql file in the folder
    for sql_file in os.listdir(sql_folder):
        if sql_file.endswith(".sql"):
            with open(os.path.join(sql_folder, sql_file), "r") as f:
                sql_content = f.read()

            try:
                cursor.executescript(sql_content)
                print(f"Successfully executed {sql_file}")
            except sqlite3.Error as e:
                print(f"An error occurred while executing {sql_file}: {e}")

    # Commit changes and close connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    import_sql_files()
