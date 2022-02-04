"""Console script for droughty."""

import typer

from dbt_test_module import schema_output

app = typer.Typer()


@app.command()
def tests():
    typer.echo(f"Generating dbt tests")

    return schema_output()


if __name__ == "__main__":
    app()

