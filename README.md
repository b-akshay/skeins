# skeins

[![PyPI](https://img.shields.io/pypi/v/skeins.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/skeins.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/skeins)][python version]
[![License](https://img.shields.io/pypi/l/skeins)][license]

[![Read the documentation at https://skeins.readthedocs.io/](https://img.shields.io/readthedocs/skeins/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/b-akshay/skeins/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/b-akshay/skeins/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/skeins/
[status]: https://pypi.org/project/skeins/
[python version]: https://pypi.org/project/skeins
[read the docs]: https://skeins.readthedocs.io/
[tests]: https://github.com/b-akshay/skeins/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/b-akshay/skeins
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

This package provides interfaces to a range of graph tasks, aiming to be: 

- **Simple** - minimal dependencies (just numpy, scipy) and lines of code
- **Fast** - especially on kNN graphs (efficient representations of manifolds). Ability to operate on graphs with 1 million nodes on a laptop. Linear algebra routines ensure scaling beyond this
- **Complete** - well-documented and tested, with usage examples on biochem and other datasets
- **Flexible** - focus on versatility of function (a range of graph tasks, and works on all graph inputs) and extensibility

Many features grew out of me wanting to use an efficient algorithm in the literature, and not finding a good implementation on the Python stack satisfying the above.






## Requirements

- TODO

## Installation

You can install _skeins_ via [pip] from [PyPI]:

```console
$ pip install skeins
```

## Usage

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_skeins_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/b-akshay/skeins/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/b-akshay/skeins/blob/main/LICENSE
[contributor guide]: https://github.com/b-akshay/skeins/blob/main/CONTRIBUTING.md
[command-line reference]: https://skeins.readthedocs.io/en/latest/usage.html
