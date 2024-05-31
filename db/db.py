import sqlite3

def create_db():
    """Connects to SQLite database, creating it if doesn't exist,
    and iterates through commands in schema to create tables. 
    Prints error message if table already exists.""" 
    con = sqlite3.connect("db/floretum.db")
    cur = con.cursor()
    with open("db/schema.sql", 'r') as f:
        schema = f.read().split("\n\n")
        for cmd in schema:
            try:
                cur.execute(cmd)
            except sqlite3.OperationalError as error:
                print(error)
                continue
    print("Database successfully created.")
    con.close()


if __name__ == "__main__":
    create_db()