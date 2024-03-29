# A very minimal example on how to run a unit test in your python project 
## 
This repository contains a minimum working example for performing unit tests and getting coverage reports for your python code.   
## Installation 
The easiest way to install the necessary libraries are through pip
``` 
python3 -m pip install --user pytest
python3 -m pip install --user coverage
python3 -m pip install --user pytest-cov
```
## Configure your code coverage
1. Create file .coveragerc in your local directory and add [run] to the very first line
2. Add files you'd like to omit from the coverage report by including omit=omitted_file1.py omitted_file2.py etc.
## Create tests
1. Create a python test file with functions name leading with "test_". All "test_*.py" files will be considered a test file and will be run
2. In the "test_" functions, call the functions that you want to test by using: assert function(argv) == expected_output
3. Add '# pragma: no cover' behind a line of function definition to exclude that line from the coverage report
## To run coverage test, do:
```
pytest --cov=. --cov-report=term-missing
```
1. you should see 100% coverage on calc_basic.py and 73% coverage on calc_advance.py. This means that every lines marked for coverage report (without # pragma: no cov) in calc_basic.py was executed and 73% of calc_advance.py was executed during the test. 
2. You should also see next to calc_advance.py missing lines: 48-53 corresponding to the lines that were not executed in the test. 
3. Notice that we did not explicitly write a test for the **factorial** function but the coverage report count it as being *executed* because the **exp** function calls **factorial**
