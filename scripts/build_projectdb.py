""" Connects to dataset, creates tables and imports data """

import os

from pprint import pprint

import psycopg2 as psql


# Read password from secrets file
# file = os.path.join("secrets", ".psql.pass")
# with open(file, "r") as file:
#     password = file.read().rstrip()

# build connection string
HOST = "hadoop-04.uni.innopolis.ru"
PORT = "5432"
USER = "team15"
DBNAME = "team15_projectdb"

PSWD = "pytttPLjPeOI7kc1"  # TODO: import from file

conn_string = f"host={HOST} port={PORT} user={USER} dbname={DBNAME} password={PSWD}"


# Connect to the remote dbms
with psql.connect(conn_string) as conn:
    # Create a cursor for executing psql commands
    cur = conn.cursor()

    # Read the commands from the file and execute them.
    with open(os.path.join("sql", "create_tables.sql"), encoding="utf-8") as file:
        content = file.read()
        cur.execute(content)

    conn.commit()

    # Read the commands from the file and execute them.
    with open(os.path.join("sql", "import_data.sql"), encoding="utf-8") as file:
        # We assume that the COPY commands in the file are ordered (1.depts, 2.emps)
        commands = file.readlines()
        with open(os.path.join("data", "processed/sliced.csv"), "r") as vehicle:
            cur.copy_expert(commands[0], vehicle)

    # If the sql statements are CRUD then you need to commit the change
    conn.commit()

    pprint(conn)
    cur = conn.cursor()

    # Read the sql commands from the file
    with open(os.path.join("sql", "test_database.sql"), encoding="utf-8") as file:
        commands = file.readlines()

        for command in commands:
            cur.execute(command)
            pprint(cur.fetchall())  # Read all records and print them
