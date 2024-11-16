import typer
from database_CLI import (
    add_record,
    update_record,
    delete_record,
    update_in_progress,
    list_records,
    update_done,
)


app = typer.Typer()


@app.command()
def add(task_string: str):
    add_record(task_string)

    print("Task added to the database")


@app.command()
def update(updated_string: str, index: int):
    update_record(updated_string, index)


@app.command()
def delete(index: int):
    delete_record(index)


@app.command()
def mark_in_progress(index: int):
    update_in_progress(index)


@app.command()
def mark_done(index: int):
    update_done(index)


@app.command()
def list_tasks(status: str):
    list_records(status)


if __name__ == "__main__":
    app()
