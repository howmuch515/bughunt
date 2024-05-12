import typer
from rich import print
from pathlib import Path
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def init(project_name: Annotated[str, typer.Argument()]):
    """Initialize a new bughunting project."""
    base_dir = Path(project_name)
    base_dir.mkdir(parents=True, exist_ok=True)

    # Create the directory structure
    (base_dir / "memo.md").touch()
    (base_dir / "scan").mkdir(exist_ok=True)
    (base_dir / "report").mkdir(exist_ok=True)
    (base_dir / "dict").mkdir(exist_ok=True)

    print(f"""Initialized new bughunting project: [bold green]\
{project_name}[/bold green] :+1:""")


@app.command(hidden=True)
def dummy():
    pass


if __name__ == "__main__":
    app()
