## Prerequisites

- Python 3.9.6
- Command line or terminal access

## Project Structure

- `secret_socities.py`: secret_socities Python script containing the algorithm.
- `graph_modified.py`: Python class for graph representation.
- `tests/`: Directory containing all test cases.
  - `testx.txt`: Test files for each test case.
- `run_tests.sh`: Bash script to run all test cases.

## Setup

1. Ensure Python 3.9.6 is installed on your system.
2. Navigate to the project's root directory in the command line or terminal.

## Running the Program

To run the program with a single test case, use the following command:

`python secret_socities.py <path-to-test-file>`

Replace `<path-to-test-file>` with the appropriate file paths.

For example:

`python secret_socities.py tests/test1.txt`

## Running All Test Cases

To run all test cases at once:

1. Make sure the `run_tests.sh` script has execute permissions:

`chmod +x run_tests.sh`

2. Execute the script:

`./run_tests.sh`

This script will automatically run the algorithm for each test case in the `tests` directory and display the results.

