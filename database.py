import sqlite3
from sqlite3.dbapi2 import Connection

from task import Task

class Database:
    # connection to the db
    conn: Connection = sqlite3.connect("db.db")

    def __init__(self, name="db.db"):
        print ("Checking if the necessary tables exist")
        self.check_tables_exist(["tasks"])
        pass

    def check_tables_exist(self, tables=[]) -> None:
        cursor = self.conn.cursor()

        stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name='%s';"
        for table in tables:
            rows = cursor.execute(stmt%table)
            if len(list(rows)):
                print ("Table `%s` exists." %table)
            else:
                print ("Table `%s` does not exist." %table)
                self.create_table("tasks", [("name", "text"), ("duration", "real"), ("priority", "real")])

    def create_table(self, table_name: str, columns: list[tuple]) -> bool:
        cursor = self.conn.cursor()
        stmt = "CREATE TABLE {table_name} ({columns})".format(table_name=table_name, columns=", ".join(map(lambda column: "%s %s"%column, columns)))
        cursor.execute(stmt)

        # add a propert stmt to check if the table is created or not
        return True

    def add_task(self, task: Task):
        cursor = self.conn.cursor()
        stmt = "INSERT INTO tasks VALUES(\"%s\", %s, %s)"%(task.get_name(), task.get_duration(), task.get_priority())
        rows = cursor.execute(stmt)
        self.conn.commit()

    def get_tasks(self) -> list:
        cursor = self.conn.cursor()
        stmt = "SELECT * FROM tasks"
        rows = cursor.execute(stmt).fetchall()
        return rows


    def __del__(self):
        self.conn.close()
