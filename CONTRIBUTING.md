Contributor's Guide
===================

To build the `py4eos` package for distribution on PyPI, first, make sure the following packages are installed:

```sh
pip install build twine
```

To build the `py4eos` distribution files:

```sh
python -m build
```

You can upload them to TestPyPI to see how the package will look:

```sh
twine upload --repository testpypi dist/*
```

Otherwise, upload to PyPI using the repo's configuration:

```sh
twine upload --repository py4eos dist/*
```

This requires having an API key configured in the file `$HOME/.pypirc`:

```
[distutils]
index-servers =
  my_project
  another_project
  ...

[my_project]
  repository = https://upload.pypi.org/legacy/
  username = __token__
  password = <API token>
```

**Additional resources:**

- [How to package Python projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Using TestPyPI](https://packaging.python.org/en/latest/guides/using-testpypi/)
