import sqlite3

import click


@click.command()
@click.option("--db-name", default="db.sqlite", help="Name of the SQLite database")
def alter_db(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    alter_sql = """
    ALTER TABLE dwa_reference ADD COLUMN classification TEXT;
    """

    cursor.executescript(alter_sql)
    print("Successfully alterned table")

    # Commit changes and close connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    alter_db()
