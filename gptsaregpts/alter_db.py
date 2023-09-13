import sqlite3

import click


def add_column(
    cursor: sqlite3.Cursor, table_name: str, column_name: str, data_type: str
) -> None:
    check_sql = f"""
    PRAGMA table_info({table_name});
    """
    columns = [column[1] for column in cursor.execute(check_sql).fetchall()]
    if column_name in columns:
        print(f"{column_name} column already exists")
        return

    alter_sql = f"""
    ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type};
    """
    cursor.executescript(alter_sql)
    print(f"Successfully added {column_name} column.")


@click.command()
@click.option("--db-name", default="db.sqlite", help="Name of the SQLite database")
def alter_db(db_name):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    add_column(cursor, "dwa_reference", "classification", "TEXT")
    for col in ["alpha", "beta", "zeta"]:
        add_column(cursor, "task_statements", col, "REAL")
        add_column(cursor, "occupation_data", col, "REAL")

    # Commit changes and close connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    alter_db()
