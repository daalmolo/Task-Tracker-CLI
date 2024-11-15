import typer

app = typer.Typer()


@app.command()
def add(task_string: str):
    pass


@app.command()
def update(index: int, updated_string: str):
    pass


@app.command()
def delete(index: int):
    pass


@app.command()
def mark_in_progress(index: int):
    pass


@app.command()
def mark_done(index: int):
    pass


@app.command()
def list_tasks(status_query: str = "all"):
    pass


if __name__ == "__main__":
    app()
