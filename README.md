# A very minimal example on how to run a unit test in your python project 
## Installs
```
pip3 install --user pytest
pip3 install --user coverage
pip3 install --user pytest-cov
```
## Configure your code coverage
1. Create file .coveragerc in your local directory and add [run] to the very first line
2. Add file you'd like to omit from coverage by including omit=omitted_file1.py omitted_file2.py etc.
## Create tests
1. Create a python test file with functions name leading with "test_"
2. In the "test_" functions, call the functions that you want to test by using: assert function(argv) == expected_output
## Run coverage
```
pytest --cov=. --cov-report=term-missing
```
