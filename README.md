# 🎄 Advent of Code
[![Tests](https://github.com/gansanay/adventofcode/actions/workflows/tests.yaml/badge.svg)](https://github.com/gansanay/adventofcode/actions/workflows/tests.yaml)
[![codecov](https://codecov.io/gh/gansanay/adventofcode/branch/main/graph/badge.svg?token=DXUOP0J9E1)](https://codecov.io/gh/gansanay/adventofcode)

This repository contains different flavors of Python 3 code for the [Advent of Code](https://adventofcode.com/) challenge, with configurations of the main tools used for ensuring programming best practices, maintainability and robustness.

## Goals for this repository

### Implementations

- `short`: the shortest implementation, counted as number of chars
- `readable`: the implementation you would be proud to commit to a production branch, linted, tested and documented
- `uppingtheante`: as a reference to this flair on [the AoC subreddit](https://www.reddit.com/r/adventofcode/), implementations where the input has been modified to become so huge that naive implementations cannot run in a reasonable time or with reasonable hardware

### Quality / Performance / Best Practices

- [x] [pre-commit](https://pre-commit.com/) configuration
- [x] tests passing
- [] 100% of code covered by tests
- [x] flake8 static analysis
- [] mypy type checking
- [] performance counters for each implementation (particularly for `uppingtheante` ones)
- [] [sphinx](https://www.sphinx-doc.org/en/master/) documentation
- [] ... with explanations of problem solving approach for each challenge

The package structure is copied from the awesome work by [Marcel Blijleven](https://github.com/marcelblijleven) in [his own Advent of Code repository](https://github.com/marcelblijleven/adventofcode).
