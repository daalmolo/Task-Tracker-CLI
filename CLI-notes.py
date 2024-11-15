import typer

app = typer.Typer()


@app.command()
def add():
    pass


@app.command()
def update():
    pass


@app.command()
def delete():
    pass


@app.command()
def mark_in_progress():
    pass


@app.command()
def mark_done():
    pass


@app.command()
def list_tasks():
    pass


if __name__ == "__main__":
    app()
