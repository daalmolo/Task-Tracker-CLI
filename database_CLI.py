import sqlite3

db_app = sqlite3.connect("notes_db.db")

notes_db_cursor = db_app.cursor()

notes_db_cursor.execute(
    """
    create table if not exists tasks_table (
    task_string text not null,
    done varchar(5) NOT NULL DEFAULT 'False',
    in_progress varchar(5) NOT NULL DEFAULT 'False'
    )
    """
)


def add_record(task):
    notes_db_cursor.execute(
        """
        insert into tasks_table (task_string) values (?)
        """,
        (task,),
    )
    db_app.commit()


def update_record(up_string, index):
    notes_db_cursor.execute(
        """
        update tasks_table
        set task_string = (?)
        where rowid = (?)
        """,
        (up_string, index),
    )
    db_app.commit()


def delete_record(index):
    notes_db_cursor.execute(
        """
        delete from tasks_table where rowid = (?)
        """,
        (index,),
    )
    db_app.commit()


def update_in_progress(index):
    notes_db_cursor.execute(
        """
        update tasks_table
        set in_progress = 'True'
        where rowid = (?)
        """,
        (index,),
    )
    db_app.commit()


def update_done(index):
    notes_db_cursor.execute(
        """
        update tasks_table
        set done = 'True', in_progress = 'False'
        where rowid = (?)
        """,
        (index,),
    )
    db_app.commit()


def list_records(constraint):
    match constraint:
        case "all":
            notes_db_cursor.execute(
                """
                select rowid, * from tasks_table 
                """
            )
        case "done":
            notes_db_cursor.execute(
                """
                select rowid, * from tasks_table 
                where done = "True"
                """
            )
        case "todo":
            notes_db_cursor.execute(
                """
                select rowid, * from tasks_table 
                where done = "False" and in_progress = "False"
                """
            )
        case "in-progress":
            notes_db_cursor.execute(
                """
                select rowid, * from tasks_table 
                where in_progress = "True"
                """
            )
        case _:
            exit()

    print("| ID \t| TASK \t\t| DONE \t| IN PROGRESS |")

    task_formatted_string = ""

    for task in notes_db_cursor.fetchall():
        for item in task:
            task_formatted_string += f"| {item}\t"

        print(f"{task_formatted_string} \t|")
        task_formatted_string = ""


db_app.commit()
