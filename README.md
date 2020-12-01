# Adrian's Advent of Code

Like an idiot, I'm going to try to do this in Python (which I know) **and** Rust
(which I don't).

## Python

Python is in a Poetry project.

To start ...

```
cd python
poetry install
poetry shell

# Run tests to get the answers
# use -s or --nocapture because the answers are printed to STDOUT by the tests
nosetests -s tests/day_01/test_advent_01.py
```
