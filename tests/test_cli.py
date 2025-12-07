import importlib

def test_cli_importable():
    # Just ensure the CLI module imports and exposes main()
    cli = importlib.import_module("blottool.cli")
    assert hasattr(cli, "main")
    assert callable(cli.main)

