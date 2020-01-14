# How to use pytest and coverage
## Installs
1. pip3 install --user pytest
2. pip3 install --user coverage
3. pip3 install --user pytest-cov
## Configure your code coverage
1. Create file .coveragerc in your local directory and add [run] to the very first line
2. Add file you'd like to omit from coverage by including omit=omitted_file1.py omitted_file2.py etc.
## Create tests
1. Create a python test file with functions name leading with "test_"
2. In the functions, call the functions that you want to test. Use assert function(argv) == expected_output
## Run coverage
1. pytest --cov=.
