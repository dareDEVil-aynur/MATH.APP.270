## Prerequisites

- Python 3.9.6
- Command line or terminal access

## Project Structure

- `flownetwork.py`: Main Python script containing the algorithm.
- `graph.py`: Python class for graph representation.
- `tests/`: Directory containing all test cases.
  - `testx.txt`: Test files for each test case.
- `run_tests.sh`: Bash script to run all test cases.

## Setup

1. Ensure Python 3.9.6 is installed on your system.
2. Navigate to the project's root directory in the command line or terminal.

## Running the Program

To run the program with a single test case, use the following command:

`python flownetwork.py <path-to-test-file>`

Replace `<path-to-test-file>` with the appropriate file paths.

For example:

`python flownetwork.py tests/test1.txt`

## Running All Test Cases

To run all test cases at once:

1. Make sure the `run_tests.sh` script has execute permissions:

`chmod +x run_tests.sh`

2. Execute the script:

`./run_tests.sh`

This script will automatically run the algorithm for each test case in the `tests` directory and display the results.

## Expected Output

Running test case 1
The 'correct answer' consists of 3 edges.
The edges are: [(43,100), (53,100), (99,100)].
Total flow through the minimum cut: 6.

---

Running test case 2
The 'correct answer' consists of 3 edges.
The edges are: [(43,100), (53,100), (99,100)].
Total flow through the minimum cut: 9.

---

Running test case 3
The 'correct answer' consists of 1 edges.
The edges are: [(3,7)].
Total flow through the minimum cut: 10.

---
