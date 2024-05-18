import typer
from rich import print
from pathlib import Path
from typing_extensions import Annotated
import tomllib
import subprocess


app = typer.Typer()
CONFIG_FILE = Path.home() / ".config" / "bughunt" / "config.toml"


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

    print(
        f"""Initialized new bughunting project: [bold green]\
{project_name}[/bold green] :+1:"""
    )


@app.command()
def scan(domain_name: Annotated[str, typer.Argument()]):
    """Scan a domain."""
    # Get scan-command from config
    if not CONFIG_FILE.exists():
        print(f"{CONFIG_FILE} not found.")
        raise typer.Exit()

    cfg = {}
    with open(CONFIG_FILE, "rb") as f:
        cfg = tomllib.load(f)
    scan_command = cfg.get("scan", {}).get("command")
    if scan_command:
        # Run the scan command with the domain_name argument
        command = scan_command.replace("{domain_name}", domain_name)
        print(f"Running scan command: {command}")
        # Execute the command
        result = subprocess.run(command, shell=True, capture_output=True)
        if result.returncode == 0:
            print("Scan completed successfully.")
        else:
            print("Scan failed.")
    else:
        print("No scan command found in the config.")
        raise typer.Exit()


if __name__ == "__main__":
    app()
