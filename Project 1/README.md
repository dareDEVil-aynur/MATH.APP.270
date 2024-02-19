## Overview

This project is designed to find the maximum number of vertices from a given set `B` that can be included on any shortest path between two vertices in a directed graph.

## Prerequisites

- Python 3.9.6
- Command line or terminal access

## Project Structure

- `assignment1_template.py`: Main Python script containing the algorithm.
- `graph.py`: Python class for graph representation.
- `tests/`: Directory containing all test cases.
  - `testgraph_x.txt`: Graph files for each test case.
  - `testset_x.txt`: Set B files for each test case.
  - `testpair_x.txt`: Pair of vertices files for each test case.
- `run_tests.sh`: Bash script to run all test cases.

## Setup

1. Ensure Python 3.9.6 is installed on your system.
2. Navigate to the project's root directory in the command line or terminal.

## Running the Program

To run the program with a single test case, use the following command:

`python assignment1_template.py <path-to-graph-file> <path-to-set-file> <path-to-pair-file>`

Replace `<path-to-graph-file>`, `<path-to-set-file>`, and `<path-to-pair-file>` with the appropriate file paths.

For example:

`python assignment1_template.py tests/testgraph_1.txt tests/testset_1.txt tests/testpair_1.txt`

## Running All Test Cases

To run all test cases at once:

1. Make sure the `run_tests.sh` script has execute permissions:

`chmod +x run_tests.sh`

2. Execute the script:

`./run_tests.sh`

This script will automatically run the algorithm for each test case in the `tests` directory and display the results.

## Expected Output

The program outputs the maximum number of vertices from set `B` on any shortest path for each test case. Results are displayed in the terminal after running the test script.
