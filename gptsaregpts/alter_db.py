import sqlite3

import click


def add_table(cursor: sqlite3.Cursor, table_name: str, sql_content: str) -> None:
    check_sql = f"""
    SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';
    """
    if cursor.execute(check_sql).fetchone():
        print(f"{table_name} table already exists")
        return

    try:
        cursor.executescript(sql_content)
        print(f"Successfully created {table_name} table.")
    except sqlite3.Error as e:
        print(f"An error occurred while creating {table_name} table: {e}")


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


BLS_ONET_SQL = """
CREATE TABLE bls_onet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    onetsoc_code CHARACTER(10) NOT NULL,
    nem_code CHARACTER(10) NOT NULL,
    nem_title TEXT NOT NULL,
    ooh_profile_code CHARACTER(10),
    ooh_profile_title TEXT,
    ooh_occupation_group TEXT,
    ooh_profile_website TEXT,
    FOREIGN KEY (onetsoc_code) REFERENCES occupation_data (onetsoc_code)
);
"""

BLS_MATRIX_SQL = """
CREATE TABLE bls_matrix (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    occupation_type TEXT NOT NULL,
    industry_type TEXT NOT NULL,
    occupation_code CHARACTER(10) NOT NULL,
    occupation_title TEXT NOT NULL,
    industry_code CHARACTER(10) NOT NULL,
    industry_title TEXT NOT NULL,
    employment_2022 REAL NOT NULL,
    percent_industry_2022 REAL NOT NULL,
    percent_occupation_2022 REAL NOT NULL,
    FOREIGN KEY (occupation_code) REFERENCES bls_onet (nem_code)
);
"""


@click.command()
@click.option("--db-name", default="db.sqlite", help="Name of the SQLite database")
def alter_db(db_name):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    # Add tables
    add_table(cursor, "bls_onet", BLS_ONET_SQL)
    add_table(cursor, "bls_matrix", BLS_MATRIX_SQL)

    # Add columns
    add_column(cursor, "dwa_reference", "classification", "TEXT")
    for col in ["alpha", "beta", "zeta"]:
        add_column(cursor, "task_statements", col, "REAL")
        add_column(cursor, "occupation_data", col, "REAL")
        add_column(cursor, "bls_matrix", col, "REAL")

    # Commit changes and close connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    alter_db()
