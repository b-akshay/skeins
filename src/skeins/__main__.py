"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """skeins."""


if __name__ == "__main__":
    main(prog_name="skeins")  # pragma: no cover
