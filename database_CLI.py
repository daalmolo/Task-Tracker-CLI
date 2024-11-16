import sqlite3

db_app = sqlite3.connect("notes_db.db")

notes_db_cursor = db_app.cursor()

var_test = False

notes_db_cursor.execute(
    """
    create table if not exists tasks_table (
    task_string text not null,
    done INTEGER NOT NULL CHECK (is_active IN (0, 1)) DEFAULT 0, 
    in_progress INTEGER NOT NULL CHECK (is_active IN (0, 1)) DEFAULT 0, 
    )
    """
)


db_app.commit()
db_app.close()
