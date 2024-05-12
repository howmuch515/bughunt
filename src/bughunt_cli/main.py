import typer
import os
from pathlib import Path

app = typer.Typer()

@app.command()
def init(project_name: str):
    """Initialize a new bughunting project."""
    base_dir = Path(project_name)
    base_dir.mkdir(parents=True, exist_ok=True)

    # Create the directory structure
    (base_dir / "memo.md").touch()
    (base_dir / "scan").mkdir(exist_ok=True)
    (base_dir / "report").mkdir(exist_ok=True)
    (base_dir / "dict").mkdir(exist_ok=True)

    typer.echo(f"Initialized new bughunting project: {project_name}")

if __name__ == "__main__":
    app()
