from hivejdbc import connect, DictCursor
import os


# Read password from secrets file
file = os.path.join("secrets", ".hive.pass")
with open(file, "r") as file:
    password = file.read().rstrip()

# Connect to HS2
conn = connect(
    host='hadoop-03.uni.innopolis.ru',
    port=10001,
    driver="/shared/hive-jdbc-3.1.3-standalone.jar",
    database='default',
    user='team15',
    password=password
)


# Create a cursor
cur = conn.cursor()

# Execute one statement
cur.execute("SHOW DATABASES")


# Here we assume that this code is written in scripts/ or notebooks/ folder in the repository folder
repo_folder = os.path.join(".")
file_path = os.path.join(repo_folder, "sql", "db.hql")


# Read line by line
with open(file_path) as file:
    for line in file.readlines():

        # see note below
        line = line.replace(";", "")
        try:
            cur.execute(line)
            print(cur.fetchall())
        except:
            pass
